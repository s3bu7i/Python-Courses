from django.urls import path
from . import views

urlpatterns = [
    
    
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),

    path("contact/",views.contact,name="contact"),

    path("xeber_panel/",views.xeber_panel,name="xeber_panel"),
    
    path("xeber_panel/news_bot/",views.news_bot,name="news_bot"),
    
    path("clear/",views.clear,name="clear"),
    
    path("news-single/<int:id>",views.news_single,name="news-single"),
    
    
    
]