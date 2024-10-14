from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


docs_view = get_schema_view(
    openapi.Info(
        title="Django REST Framework API",
        default_version='v1',
        description="API for Django REST Framework",
        contact=openapi.Contact(email="dvoraj75@gmail.com"),
        license=openapi.License(name="MIT License", url="../LICENSE"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("introduction_api.apps.user.urls")),
    path("auth/", include("django.contrib.auth.urls")),

    path('swagger/', docs_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', docs_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
