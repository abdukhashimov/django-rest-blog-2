from django.urls import path, include

from post.views import PostListView, PostDetailView


# app_name = 'post'
urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail')
]
