from django.contrib import admin
from django.urls import path
from . import views

#http://127.0.0.1:8000/


urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('blogs/', views.blogs),
    path('blogs/int:<id>', views.blog_details),
]
