from django.contrib import admin

from post.models import PostModel


@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]
