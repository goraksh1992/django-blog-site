from django.urls import path
from . import views


urlpatterns = [

    # path('', views.blog_home, name="blog-home"),
    path('', views.PostListView.as_view(), name="blog-home"),
    path('create-new-post', views.PostCreateView.as_view(), name="create-new-post"),
    path('post-detail/<int:pk>', views.PostDetailView.as_view(), name="post-detail"),
    path('update-post/<int:pk>', views.PostUpdateView.as_view(), name="update-post"),
    path('delete-post/<int:pk>', views.PostDeleteView.as_view(), name="delete-post"),
    path('user-post/<str:username>', views.UserPostListView.as_view(), name="user-post"),
]