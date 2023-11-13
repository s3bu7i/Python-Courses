import requests
from bs4 import BeautifulSoup as bs

path = "https://apa.az"


headers_parame={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0"}

request = requests.get(path,headers=headers_parame)

# print(request.content)


soup = bs(request.content,"html.parser")

news = soup.find("div",class_ = "news")
for x in news:
    
    try:
        link = x["href"]
        
        req = requests.get(link)
        data = bs(req.content,"html.parser")

        category = data.find("div",class_="breadcrumb_row").find("h1").text
        # print(category)
        foto = data.find("div",class_="main_img").find("img")
        
        # print(foto["src"])
        
        hava = data.find("div",attrs={"class":"weather_navbar-currency"}).find_all("p")[1]
        
        print(foto["src"],category,hava.text)
        

    except:TypeError

# print(soup.prettify())

# category = soup.find("ul",class_ = "links").find_all("li")[1].text


# parent = soup.find("div",class_ = "title" ).find_parent()


# metn = soup.find("div",class_ = "title" ).find("h1").text

# print(metn)







