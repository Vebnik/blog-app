from rest_framework import serializers


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    author = serializers.CharField()
    content = serializers.CharField()
    created_at = serializers.DateTimeField()
