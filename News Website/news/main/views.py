from django.shortcuts import render, redirect
from django.urls import reverse
from bs4 import BeautifulSoup as bs
from django.http import HttpResponseRedirect
import requests
from . models import News_data


# Create your views here.


def xeber_panel(request):

    news = News_data.objects.all()
    count = News_data.objects.all().count()
    context = {

        'news': news,
        'count': count

    }
    return render(request, "main/xeber_panel.html", context)


def news_bot(request):

    data = requests.get("https://lent.az")

    url = bs(data.text, "html.parser")

    soup = url.find("div", class_="all-news-wrapper")

    for x in soup:

        text = ''
        category = ''
        date = ''
        image = ''
        weather = ''
        title = ''

        try:

            link = x["href"]

            data1 = requests.get(link)
            soup1 = bs(data1.text, "html.parser")

            category = soup1.find("div", class_="breadcrumb_row").text

            date = soup1.find("div", class_="overlay").text.replace(
                "(UTC +04:00)", "")

            title = soup1.find("h1", class_="news_title").text

            text = soup1.find("div", class_="news_content").find("p").text

            image = soup1.find("div", class_="news_img").find("img")

            weather = soup1.find(
                "div", class_="top_section").find_all("li")[3].text

            print(image)

        except:
            TypeError

        News_data(img=image).save()

    return HttpResponseRedirect(reverse("xeber_panel"))


def home(request):

    return render(request, "main/home.html")


def about(request):
    return render(request, "main/about.html")


def contact(request):
    return render(request, "main/contact.html")





