from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.exceptions import APIException

from post.serializers import PostDetailSerializer, PostListSerializer
from post.service import PostService, PostRepositoryFilter


class PostListView(ListAPIView):
    serializer_class = PostListSerializer
    service = PostService

    def get_queryset(self):
        filter_by: str | None = self.request.query_params.get("filter_by")  # type: ignore
        filter_value: str | None = self.request.query_params.get("value")  # type: ignore
        order_by: str | None = self.request.query_params.get("order_by", "created_at")  # type: ignore
        desc: bool = self.request.query_params.get("desc", "True") == "True"  # type: ignore

        filters = PostRepositoryFilter(
            filter_by=filter_by,
            value=filter_value,
            order_by=order_by,
            desc=desc,
        )

        posts = self.service.get_all_by_filter(filters)

        if not posts:
            APIException.status_code = status.HTTP_404_NOT_FOUND
            raise APIException("Not found posts", "error")

        return posts


class PostDetailView(RetrieveAPIView):
    serializer_class = PostDetailSerializer
    service = PostService

    def get_object(self):
        pk: int = self.kwargs["pk"]
        post = self.service.get_by_pk(pk)

        if post is None:
            APIException.status_code = status.HTTP_404_NOT_FOUND
            raise APIException("Not found post", "error")

        return post
