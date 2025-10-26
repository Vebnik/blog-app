from django.contrib import admin
from blog.models import PostModel, CommentModel


@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]
