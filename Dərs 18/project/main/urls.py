from django.urls import path
from . import views


urlpatterns = [


    path('', views.index, name='index'),
    path('haqqinda/', views.about, name='about'),
    path('elaqe/', views.elaqe, name='elaqe'),
    path('calculator/', views.calculator, name='calculator'),
    path('login/', views.login, name='login'),
    path('radio/', views.radio, name='radio'),
    path('exam/', views.exam, name='exam'),
    path('select/', views.select, name='select'),
    path('select_exchange/', views.select_exchange, name='select_exchange'),
    path('army/', views.step, name='step'),
    path('crud/', views.crud, name='crud'),
    #path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('tesdiq/int:id', views.tesdiq, name='tesdiq'),






]
