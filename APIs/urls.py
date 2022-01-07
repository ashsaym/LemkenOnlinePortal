from django.contrib import admin
from django.urls import path, include
from APIs import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import routers

router = routers.DefaultRouter()
router.register('ping', views.PingViewSet, basename="ping")
router.register('connect', views.ConnectCheckViewSet, basename="connect")
router.register('Connect/Check', views.ConnectionCheck, basename="ConnectionCheck")
router.register('licences/list', views.ShowLicenceDetailsView, basename="licencesView")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/token/get/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/renew/', TokenRefreshView.as_view(), name='token_get_access'),

    path('api/CommunicationUnit/List/', views.CommunicationUnitListView.as_view(), name='CommunicationUnitListView'),
    path('api/CommunicationUnit/Details/<str:pk>', views.CommunicationUnitDetailView.as_view(),
         name='CommunicationUnitDetails'),

    path('api/licences/check/status/<str:Serial_Number>&&<str:license_type>',
         views.ShowOneLicenceDetailsForMachine),
    path('api/', include(router.urls))
]
