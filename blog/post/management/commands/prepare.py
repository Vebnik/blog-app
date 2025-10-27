from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.db import connection


class Command(BaseCommand):
    help = "Prepare data for app"

    def handle(self, *args, **options):
        try:
            with connection.cursor() as cursor:

                # create admin user
                cursor.execute(
                    """
                    insert into auth_user (username, email, first_name, last_name, password, is_superuser, is_staff, is_active, date_joined)
                    values (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    returning id;
                    """,
                    [
                        "admin",
                        "admin@email.com",
                        "admin_name",
                        "",
                        make_password("admin"),
                        True,
                        True,
                        True,
                        timezone.now(),
                    ],
                )

                print("Admin user crated")

                # create posts and comment
                for i in range(100):
                    cursor.execute(
                        f"""
                        insert into post_postmodel (title, description, content, created_at, author_id)
                        values({i}, 'description - {i}', 'content - {i}', '{timezone.now()}', 1)
                        returning id
                        """
                    )

                    post_id = cursor.fetchone()

                    if post_id is None:
                        continue

                    post_id = post_id[0]

                    for i in range(10):
                        cursor.execute(
                            f"""
                            insert into public.comment_commentmodel
                            (author, "content", created_at, post_id)
                            values('Admin', 'content - {i}', '{timezone.now()}', {post_id});
                            """
                        )

                print("Posts created")

        except Exception as error:
            print(error)
