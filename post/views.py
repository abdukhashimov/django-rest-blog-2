from post.models import Post
from rest_framework.permissions import AllowAny
from post.serializers import PostListSerializer, PostDetailSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from post.pagination import PostLimitOffsetPagination, PostPageNumberPagination


class PostListView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    permission_classes = [AllowAny, ]
    pagination_class = PostPageNumberPagination


class PostDetailView(RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    permission_class = [AllowAny, ]
