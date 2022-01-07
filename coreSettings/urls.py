from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Users.urls')),
    path('', include('SiteLogs.urls')),
    path('', include('CommunicationUnits.urls')),
    path('', include('Licences.urls')),
    path('', include('APIs.urls'))

]
