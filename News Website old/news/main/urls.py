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
    
    path("search/",views.search,name="search"),
    
    path("news/",views.news,name="news"),
    
    
    
    path("register/",views.register,name="register"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),

    
    path('edit/<int:id>',views.edit,name="edit"),
    
    path('update/<int:id>',views.update,name="update"),
    
    
    
    
    
    path('active/<int:id>',views.active,name="active"),
    
    path('block/<int:id>',views.block,name="block"),



   
    
    
    
    
]