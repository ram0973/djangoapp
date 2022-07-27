from rest_framework import generics
from rest_framework.response import Response

from blog.models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        data = super().list(self, request, *args, **kwargs).data
        data = dict(articles=data)
        return Response(data)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        data = super().get(self, request, *args, **kwargs).data
        data = dict(article=data)
        return Response(data)
