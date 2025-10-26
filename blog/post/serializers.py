from rest_framework import serializers

from comment.serializers import CommentSerializer


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    username = serializers.CharField()
    email = serializers.EmailField()


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    title = serializers.CharField(max_length=1024)
    author = AuthorSerializer()
    image = serializers.ImageField(required=False)
    created_at = serializers.DateTimeField(required=False)


class PostListSerializer(PostSerializer):
    description = serializers.CharField()
    last_comment_date = serializers.DateTimeField(required=False)
    last_comment_author = serializers.CharField(required=False)


class PostDetailSerializer(PostSerializer):
    comments = CommentSerializer(many=True)
    content = serializers.CharField()
