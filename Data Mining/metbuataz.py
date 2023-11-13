import requests
from bs4 import BeautifulSoup as bs


path = "https://metbuat.az/news/1484577/ilham-eliyevin-receb-tayyib-erdogan-ile-gorusu-olub.html"


headers_parame = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0"}


request = requests.get(path, headers=headers_parame)


soup = bs(request.content, "html.parser")


text = soup.find("article", attrs={"class": "normal-text"}).find("strong").text

category = soup.find("span", class_="news_in_catg").find("a").text


img = soup.find("div", class_="fix").find("img")

title = soup.find("h1", class_="news_in_ttl").text

# print(title)

hava = soup.find("span", attrs={"data-bind": "label"}).text.strip()


print(text, category, img["src"], title, hava)


# print("https://metbuat.az" +img["src"])
