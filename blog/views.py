from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from .models import Post, Category, Tag, Comment
from .forms import CommentForm


# Create your views here.


class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()

        return context
    
class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title','hook_text','content','head_image','file_upload','category','tags']

    template_name = 'blog/post_update_form.html'

    def get_context_data(self, **kwargs):
        context = super(PostUpdate, self).get_context_data()
        if self.object.tags.exists():
            tags_str_list = list()
            for t in self.object.tags.all():
                tags_str_list.append(t.name)
            context['tags_str_default'] = ';'.join(tags_str_list)
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
        
    def form_valid(self, form):
        response = super(PostUpdate, self).form_valid(form)
        self.object.tags.clear()

        tags_str = self.request.POST.get('tags_str')
        if tags_str:
            # 입력한 str 공백제거
            tags_str = tags_str.strip()

            # , ; 둘 다 가능하게 함
            tags_str = tags_str.replace(',',';')
            tags_list = tags_str.split(';')

            for t in tags_list:
                t = t.strip()

                if t == "":
                    continue
                # 있으면 가져오고 없으면 만드는 함수
                tag, is_tag_created = Tag.objects.get_or_create(name=t)
                # 만약 없는 태그값을 받아왔다면 만든다
                if is_tag_created:
                    tag.slug = slugify(t, allow_unicode=True)
                    tag.save()
                self.object.tags.add(tag)

        return response

    
class PostCreate(LoginRequiredMixin, UserPassesTestMixin,CreateView):
    model = Post
    fields = ['title','hook_text','content','head_image','file_upload','category','tags']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            response = super(PostCreate, self).form_valid(form)

            tags_str = self.request.POST.get('tags_str')
            if tags_str:
                tags_str = tags_str.strip()
                
                tags_str = tags_str.replace(',',';')
                tags_list = tags_str.split(';')

                for t in tags_list:
                    t= t.strip()

                    if t == "":
                        continue
                    tag, is_tag_created = Tag.objects.get_or_create(name=t)
                    if is_tag_created:
                        tag.slug = slugify(t, allow_unicode=True)
                        tag.save()
                    self.object.tags.add(tag)
            return response

        else:
            return redirect('/blog/')

def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    return render(request, 'blog/post_list.html', {
        'post_list':post_list,
        'tag':tag,
        'categories':Category.objects.all(),
        'no_category_post_count':Post.objects.filter(category=None).count(),
    })


def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request, 'blog/post_list.html',{
            'post_list':post_list,
            'categories':Category.objects.all(),
            'no_category_post_count':Post.objects.filter(category=None).count(),
            'category':category
        }
    )

# def index(request):
#     posts = Post.objects.all().order_by('-pk')


#     return render(request, 'blog/index.html',{'posts':posts})

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['comment_form'] = CommentForm

        return context


# def post_detail(request, pk):
#     post = Post.objects.get(pk=pk)

#     return render(request, 'blog/post_detail.html', {'post':post})


def new_comment(request, pk):
    # 로그인했는지 확인
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        # method가 POST일경우 CommentForm 값을 불러온다
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                # 작성버튼 누르면 페이지로 리다이렉트
                return redirect(comment.get_absolute_url())
        else:
            return redirect(post.get_absolute_url())
    else:
        # 로그인하지 않았다면 PermissionDenied 권한이 거부됨
        raise PermissionDenied
    

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm

    # GET인지 POST인지 판단하는 함수
    def dispatch(self, request, *args, **kwargs):
        # 작성자인지 아닌지 구별해서 실행하게함
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
        else:
            # 작성자 아니면 오류나게함
            raise PermissionDenied
        
def delete_comment(request, pk):
    # delete_comment 함수에서 인자로받은 pk을받고 comment변수에 넣음 만약 객체가 존재하지않는다면 404예외오류 발생시킴
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post
    # 로그인한 방문자와 작성자가 같으면 실행
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        return redirect(post.get_absolute_url())
    else:
        # 아니면 오류
        raise PermissionDenied