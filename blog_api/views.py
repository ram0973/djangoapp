from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer, PostListSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostListSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
