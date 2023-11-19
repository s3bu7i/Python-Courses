from django.shortcuts import render ,redirect
from django.urls import reverse
from bs4 import BeautifulSoup as bs
from django.http import HttpResponseRedirect
import requests
from . models import *
from django.db.models import Q , Count , Sum




# Create your views here.

def clear(request):
    News_data.objects.all().delete()
    return HttpResponseRedirect(reverse("xeber_panel"))


def xeber_panel(request):
    
    
    
    
    news = News_data.objects.all()
    count = News_data.objects.all().count()
    
    context = {
        
        'news': news,
        'count': count,
        
        
    }
    return render(request, "main/xeber_panel.html",context)



def news_bot(request):

    data = requests.get("https://lent.az")

    url = bs(data.text,"html.parser")

    soup = url.find("div",class_ = "all-news-wrapper")

    for x in soup:
        
        
        try:
            
            link = x["href"]
            
            data1 = requests.get(link)
            soup1 = bs(data1.text,"html.parser")
            
            category = soup1.find("div",class_ = "breadcrumb_row").find('h3').text
            
            date = soup1.find("div",class_ = "overlay").text.replace("(UTC +04:00)","")
            
            title = soup1.find("h1",class_ = "news_title").text
            
            text = soup1.find("div",class_ = "news_content").text
            # text = ''.join(map(str,text))

            
            image = soup1.find("div",class_ = "news_img").find("img")
            
            image = image["src"]
            
            
            
            weather = soup1.find("div",class_ = "top_section").find_all("li")[3].text            

            
            
        
            News_data(text=text,title=title,date=date,category=category,weather=weather,img=image).save()

        
        
       
            
           

       
        except:TypeError
        
        

    
    return HttpResponseRedirect(reverse("xeber_panel"))


def home(request):
    
    idman = News_data.objects.raw("SELECT * FROM main_news_data WHERE category == 'İDMAN' ")
    
    
    category = News_data.objects.raw("SELECT * FROM main_news_data GROUP BY category")
    
    
    # select_related
    # prefetch_related
    
    # category = Test.objects.prefetch_related()

    
    # category = Test.objects.select_related()
    
    
    
    
    latest = News_data.objects.all()[3:7]
    news01 = News_data.objects.all()[0:1]
    news02 = News_data.objects.all()[1:3]
    news03 = News_data.objects.all()[3:7]
    news04 = News_data.objects.all()[7:11]


    data = News_data.objects.all()[0:4]
    context = {
        
        "data":data,
        'news01':news01,
        "news02":news02,
        "latest":latest,
        'category':category,
        "idman":idman,
        "news03":news03,
        "news04":news04
        
        
    }
    return render(request,"main/home.html",context)


def news_single(request,id):
    news = News_data.objects.filter(id=id)
    
    context = {
        
        'news':news
        
    }
    return render(request,"main/news-single.html",context)


def about(request):
    return render(request,"main/about.html")



def contact(request):
    return render(request,"main/contact.html")


def search(request):
    if request.method == 'POST':
        q = request.POST["search"]
        
        search = News_data.objects.filter(Q(title__contains = q)| Q(text__contains = q)|Q(category__contains = q))
            
            
        count = search.count()
        
    context = {
        
        'search':search,
        'count':count
       
        
    }
    
    
    return render(request,"main/search.html",context)