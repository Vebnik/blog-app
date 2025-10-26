from dataclasses import dataclass
from django.db import connection


base_query = """
    select
        pp.id,
        pp.title,
        pp.description,
        pp.content,
        pp.image,
        pp.created_at,
        pp.author_id,
        au.username,
        au.email,
        (
            select
                json_agg(
                    json_build_object(
                        'id', cc.id,
                        'author', cc.author,
                        'content', cc.content,
                        'created_at', cc.created_at,
                        'post_id', cc.post_id
                    )
                    order by cc.created_at desc
                )
            from comment_commentmodel cc
            where cc.post_id = pp.id
            {limit}
        ) as last_comment
    from post_postmodel pp
    inner join auth_user au on pp.author_id = au.id
    {append_query}
"""


@dataclass
class PostRepositoryFilter:
    filter_by: str | None
    value: str | None
    order_by: str | None
    desc: bool


class PostRepository:
    @staticmethod
    def get_by_pk(pk: int):
        with connection.cursor() as cursor:
            append_query = f"where pp.id = {pk}"

            print(base_query.format(append_query=append_query, limit=""))

            cursor.execute(base_query.format(append_query=append_query, limit=""))
            return cursor.fetchone()

    @staticmethod
    def get_all_with_filter(filter: PostRepositoryFilter):
        with connection.cursor() as cursor:

            append_query = ""

            allow_fields = [
                "created_at",
                "id",
                "email",
                "username",
                "title",
                "author_id",
            ]

            if filter.filter_by and filter.value and filter.filter_by in allow_fields:
                append_query += f"where {filter.filter_by} = '{filter.value}'\n"
            if filter.order_by and filter.order_by in allow_fields:
                append_query += f"order by {filter.order_by} desc"

            cursor.execute(
                base_query.format(append_query=append_query, limit="limit 1")
            )
            return cursor.fetchall()
