from django.urls import path

from post.apps import PostConfig
from post.views import PostListView, PostDetailView

app_name = PostConfig.name

urlpatterns = [
    path("list/", PostListView.as_view(), name="post-list"),
    path("detail/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
