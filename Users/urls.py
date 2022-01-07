from django.urls import path
from Users import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
