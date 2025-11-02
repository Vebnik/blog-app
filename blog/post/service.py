from post.repository import PostRepository, PostRepositoryFilter


class PostService:
    @staticmethod
    def get_by_pk(pk: int):
        raw_data = PostRepository.get_by_pk(pk)

        if raw_data is None:
            return None

        data = {
            "id": raw_data[0],
            "title": raw_data[1],
            "description": raw_data[2],
            "content": raw_data[3],
            "image": raw_data[4],
            "created_at": raw_data[5],
            "author": {
                "id": raw_data[6],
                "username": raw_data[7],
                "email": raw_data[8],
            },
            "comments": raw_data[9],
        }

        return data

    @staticmethod
    def get_all_by_filter(filter: PostRepositoryFilter):
        raw_data = PostRepository.get_all_with_filter(filter)

        data = list(
            map(
                lambda row: {
                    "id": row[0],
                    "title": row[1],
                    "description": row[2],
                    "image": row[4],
                    "created_at": row[5],
                    "author": {
                        "id": row[6],
                        "username": row[7],
                        "email": row[8],
                    },
                    "last_comment_date": (
                        row[9][0]["created_at"] if row[9] is not None else None
                    ),
                    "last_comment_author": (
                        row[9][0]["author"] if row[9] is not None else None
                    ),
                },
                raw_data,
            )
        )

        return data
