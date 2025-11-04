from rest_framework import serializers

from app.settings import MEDIA_URL
from comment.serializers import CommentSerializer


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    username = serializers.CharField()
    email = serializers.EmailField()


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    title = serializers.CharField(max_length=1024)
    author = AuthorSerializer()
    image = serializers.SerializerMethodField(required=False)
    created_at = serializers.DateTimeField(required=False)

    def get_image(self, obj):
        return f"{MEDIA_URL}{obj["image"]}" if obj["image"] is not None else None


class PostListSerializer(PostSerializer):
    description = serializers.CharField()
    last_comment = CommentSerializer()


class PostDetailSerializer(PostSerializer):
    comments = CommentSerializer(many=True)
    content = serializers.CharField()
