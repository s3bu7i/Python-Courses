from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('register/', views.register, name='register'),

    path('login/', views.login, name='login'),


    path('logout/', views.logout, name='logout'),

    path('settings/', views.settings_profile, name='settings_profile'),


    path('updateprofile/<int:id>', views.updateprofile, name='updateprofile'),

    path('block/<int:id>', views.block, name='block'),


    path('active/<int:id>', views.active, name='active'),

    path('send__mail/', views.send__mail, name='send__mail'),

    path('delete/<int:id>', views.delete, name='delete'),

]
