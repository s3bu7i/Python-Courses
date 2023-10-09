from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
   
    path('register/',views.register,name='register'),
    
    path('login/',views.login,name='login'),
    
    
    path('logout/',views.logout,name='logout'),
    
    path('settings/',views.settings,name='settings'),   
    
    
    path('updateprofile/<int:id>',views.updateprofile,name='updateprofile'),
    
    path('block/<int:id>',views.block,name='block'),

]   