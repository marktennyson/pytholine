from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('login-api/', views.login_api),
    path('signup/', views.signup),
    path('signup-api/', views.signup_api),
]