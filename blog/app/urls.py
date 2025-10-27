from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


from app.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    # drf
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api-auth/", include("rest_framework.urls")),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # post
    path("api/post/", include("post.urls")),
]

urlpatterns = urlpatterns + static(MEDIA_URL, document_root=MEDIA_ROOT)
