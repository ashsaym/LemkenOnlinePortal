from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('token/get/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/renew/', TokenRefreshView.as_view(), name='token_get_access')
]
