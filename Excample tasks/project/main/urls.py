from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.index,name='index'),
    path('haqqinda/',views.about,name='about'),
    path('elaqe/',views.elaqe,name='elaqe'),
    path('calculator/',views.calculator,name='calculator'),
    
    
    
]