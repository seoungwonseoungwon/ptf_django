from django.urls import path
from . import views


urlpatterns = [
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('tag/<str:slug>/', views.tag_page),
    path('category/<str:slug>/', views.category_page),
    path('',views.PostList.as_view(), name="blog"),
    path('<int:pk>/',views.PostDetail.as_view(), name="post_detail"),
    path('<int:pk>/new_comment/', views.new_comment),
]