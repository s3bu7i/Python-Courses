from django.urls import path
#from . import views
from main import views

urlpatterns = [
    path('', views.index, name = 'index'),
    
    
]

