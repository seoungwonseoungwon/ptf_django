from django.urls import path
from . import views


urlpatterns = [
    path('category/<str:slug>/', views.category_page),
    path('',views.PostList.as_view(), name="blog"),
    path('<int:pk>/',views.PostDetail.as_view(), name="post_detail"),
]