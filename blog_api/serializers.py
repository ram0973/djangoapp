from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status',)
        # list_serializer_class = PostListSerializer


class PostListSerializer(serializers.ListSerializer):
    child = PostSerializer

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret = dict(articles=ret)
        return ret

    def update(self, instance, validated_data):
        super().update(self, instance, validated_data)
