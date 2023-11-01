from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('sign_up/', views.signup, name="sign_up"),
    path('sign_in/', views.sign_in, name="sign_in"),
    path('log_out/', views.log_out, name="log_out"),
    path('crud/', views.crud, name="crud"),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),


    
]