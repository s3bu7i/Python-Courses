# apps/accounts/urls.py
from django.urls import path
from .views import register, login


urlpatterns = [
path('auth/register', register),
path('auth/login', login),
]