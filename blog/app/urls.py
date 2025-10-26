from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from .settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    # drf
    path("api-auth/", include("rest_framework.urls")),
    # post
    path("api/post/", include("post.urls")),
]

urlpatterns = urlpatterns + static(MEDIA_URL, document_root=MEDIA_ROOT)
