from django.urls import path
from . import views


urlpatterns = [
    
    
    path('',views.index,name='index'),
    path('haqqinda/',views.about,name='about'),
    path('elaqe/',views.elaqe,name='elaqe'),
    path('calculator/',views.calculator,name='calculator'),
    path('login/',views.login,name='login'),
    path('radio/',views.radio,name='radio'),
    path('exam/',views.exam,name='exam'),
    path('select/',views.select,name='select'),
    path('select_exchange/',views.select_exchange,name='select_exchange'),
    path('army/',views.step,name='step'),

    path('crud/',views.crud,name='crud'),
    
    # path('delete/',views.delete,name='delete'),
    
    path('delete/<int:pk>',views.delete,name='delete'),
    
    path('edit/<int:id>',views.edit,name='edit'),
    
    path('update/<int:id>',views.update,name='update'),
    
    
    path('tesdiq/<int:id>',views.tesdiq,name='tesdiq'),
    
    
    path('telefon/',views.telefon,name='telefon'),
    
    
    # path('etrafli/<int:pk>',views.Etrafli.as_view(),name='etrafli'),

    path('etrafli/<int:id>',views.etrafli,name='etrafli'),
    
    path('shop/',views.shop,name='shop'),
    
    path('item/',views.item,name='item'),
    
    path('axtar/',views.axtar,name='axtar'),

 
   
]