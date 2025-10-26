from django.contrib import admin

from comment.models import CommentModel


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at"]
