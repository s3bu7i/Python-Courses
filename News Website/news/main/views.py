from django.shortcuts import render ,redirect,get_object_or_404
from django.urls import reverse
from bs4 import BeautifulSoup as bs
from django.http import HttpResponseRedirect
import requests
import json
from . models import *
from django.db.models import Q , Count , Sum
from django.core.paginator import Paginator
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.db.models import Count




def active(request,id):
    data = News_data.objects.get(id=id)
    data.is_active = 1
    data.save()
    return redirect("xeber_panel")

def block(request,id):
    data = News_data.objects.get(id=id)
    data.is_active = 0
    data.save()

    return redirect("xeber_panel")




def edit(request,id):
    
    edit = News_data.objects.get(id=id)
    
    
    context = {
        
        'edit':edit
        
    }
    return render(request,"main/xeber_panel.html",context)


def update(request,id):
    
    if request.method == 'POST':
        text = request.POST["text"]
        category = request.POST["category"]
        title = request.POST["title"]
        
        data = News_data.objects.get(id=id)
        
        data.text = text
        data.title = title
        data.category = category
        data.save()
        
    return redirect("xeber_panel")
        
        


def register(request):
    generated_password = User.objects.make_random_password(length=15,allowed_chars="qwErtyuioPasdfgHjklZxcvbnm1234567890!@#$%^&*90-=><?/~")

    if request.method == 'POST':
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]
        
        if pass1 == pass2:
            
            if User.objects.filter(username=username).exists():
                messages.info(request,"Bu istifadeci hal-hazirda movcuddur")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Bu email hal-hazirda movcuddur")
            else:
                
                User.objects.create_user(username=username, email=email, password=pass2,first_name=first_name,last_name=last_name).save()
                
                return redirect("login")
            
        else:
            messages.info(request,"Parollar uygun deyil")

            
            
    return render(request,"main/register.html",{"generated_password":generated_password})

def login(request):
    
    if request.method == "POST":
        
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(username=username,password=password)
        
        if user is not None:
            
            auth.login(request,user)
    
    
            return redirect("xeber_panel")
    
    return render(request,"main/login.html")


def logout(request):
    auth.logout(request)
    return redirect("login")

@login_required(login_url='login')
def clear(request):
    News_data.objects.all().delete()
    return HttpResponseRedirect(reverse("xeber_panel"))


@login_required(login_url='login')
def xeber_panel(request):
    
    
    
    
    news = News_data.objects.all()
    count = News_data.objects.all().count()
    
    context = {
        
        'news': news,
        'count': count,
        
        
    }
    
    return render(request, "main/xeber_panel.html",context)


@login_required(login_url='login')
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
            
            category = category.replace("Maraq",category.upper())
            
            date = soup1.find("div",class_ = "overlay").text.replace("(UTC +04:00)","")
            
            title = soup1.find("h1",class_ = "news_title").text
            
            text = soup1.find("div",class_ = "news_content").text
            # text = ''.join(map(str,text))
            
            text = text.replace("Lent.az","")
            
           
            
            image = soup1.find("div",class_ = "news_img").find("img")
            
            image = image["src"]
            
            
            
            weather = soup1.find("div",class_ = "top_section").find_all("li")[3].text            

            response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Baku&appid=99a41dbd8a4f2daca52453c067961160")
            data = response.text




            data = json.loads(data)




            weather = data["main"]["temp"] - 273.15
            
            weather = round(weather)
            
        
            News_data(text=text,title=title,date=date,category=category,weather=weather,img=image).save()

        
        
       
            
           

       
        except:TypeError
        
        

    
    return HttpResponseRedirect(reverse("xeber_panel"))





def home(request):
    
    
    
    
    running_text = News_data.objects.all()[11:14]
    
    idman = News_data.objects.raw("SELECT * FROM main_news_data WHERE category == 'İDMAN' AND is_active == 1 ORDER BY id DESC LIMIT 0,4 ")
    
    
    
    category = News_data.objects.raw("SELECT * FROM main_news_data GROUP BY category LIMIT 0,8")
    
    
    # select_related
    # prefetch_related
    
    # category = Test.objects.prefetch_related()

    
    # category = Test.objects.select_related()
   
    
    
    latest = News_data.objects.filter(is_active = 1).order_by("-id")[3:7]
    
    news01 = News_data.objects.filter(is_active = 1).order_by("-id")[0:1]
    
    news02 = News_data.objects.filter(is_active = 1).order_by("-id")[1:3]
    news03 = News_data.objects.filter(is_active = 1).order_by("-id")[3:7]
    news04 = News_data.objects.filter(is_active = 1).order_by("-id")[7:11]


    data = News_data.objects.filter(is_active = 1).order_by("-id")[0:4]
    
    weather = News_data.objects.last()
    
    context = {
        
        "data":data,
        'news01':news01,
        "news02":news02,
        "latest":latest,
        'category':category,
        "idman":idman,
        "news03":news03,
        "news04":news04,
        "weather":weather,
        'running_text':running_text
        
        
    }
    
    return render(request,"main/home.html",context)


def category(request,id):
    cate = News_data.objects.values("category").distinct().annotate(say=Count("category"))[0:5]
    
    cat = News_data.objects.values("category").distinct()[0:10]
    
    data = News_data.objects.get(id=id)
    a = data.category
    
    test = News_data.objects.filter(category=a)
    
    c = test.last()
    
    context = {
        
        'test':test,
        'cate':cate,
        'cat':cat,
        'c':c
        
    }
    
    return render(request,"main/category.html",context)

# get_object_or_404 ya obyekti geri qaytarir ya da(yoxdursa) 404 sehifesine gedir

def news_single(request,id):
    
    news = News_data.objects.filter(id=id)
    
    viewer = get_object_or_404(News_data, id=id)

    
    ip_address = request.ip_address
    
    
    session_key = f'viewed_article_{id}_by_ip_{ip_address}'
    
    if session_key not in request.session:
        viewer.view += 1
        viewer.save()
        request.session[session_key] = True
    
   
    
    context = {
        
        'news':news,
        
    }
    
    return render(request,"main/news-single.html",context)


def about(request):
    return render(request,"main/about.html")



def contact(request):
    return render(request,"main/contact.html")


def search(request):
    
    cate = News_data.objects.values("category").distinct().annotate(say=Count("category"))[0:5]
    
    cat = News_data.objects.values("category").distinct()[0:10]


    search = ''
    count = ''
    
    if request.method == 'POST':
        q = request.POST["search"]
        
        search = News_data.objects.filter(Q(title__contains = q)| Q(text__contains = q)|Q(category__contains = q))
            
            
        count = search.count()
        
    context = {
        
        'search':search,
        'count':count,
        'cate':cate,
        'cat':cat
   
        
    }
    
    
    return render(request,"main/search.html",context)


def news(request):
    idman = News_data.objects.raw("SELECT * FROM main_news_data WHERE category == 'İDMAN' ")
    
    category = News_data.objects.raw("SELECT * FROM main_news_data GROUP BY category")
    
    # Sehifede 10 xeber gorsenecek
    x = Paginator(News_data.objects.all().order_by("-id"),10)
    
    # sehifeni cevirdikce Linkde gorsenecek deyishen adi  , meselen : seh=2
    page = request.GET.get("seh")
    
    # Her sehifesinde 10 melumat saxlayan , icinde xeberlerin oldugu deyishen(fora salacagimiz)
    news_page = x.get_page(page)
    
    # Sehifeler
    page_range = x.page_range
    
    context = {
        
        'category':category,
        "idman":idman,
        "news_page":news_page,
        "page_range":page_range,
        
        
    }
    
    
    return render(request,"main/news.html",context)


def error_page(request,exception):
    
    return render(request,"404.html",status=404)