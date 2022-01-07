from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Lemken Online API",
      default_version='v1',
      description="Lemken Online API for Product IT",
      terms_of_service="https://api.iqblue.digital/policies/terms/",
      contact=openapi.Contact(email="admin@iqblue.digital"),
   ),
   public=True,
   permission_classes=[permissions.IsAuthenticated],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('', include('Users.urls')),
    path('', include('SiteLogs.urls')),
    path('', include('CommunicationUnits.urls')),
    path('', include('Licences.urls')),
    path('', include('APIs.urls'))

]
