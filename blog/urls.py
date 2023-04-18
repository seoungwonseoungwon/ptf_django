from django.urls import path
from . import views


urlpatterns = [
    # path('',views.index, name="blog"),
    path('',views.PostList.as_view(), name="blog"),
    path('<int:pk>/',views.post_detail, name="post_detail"),
]