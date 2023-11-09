import requests
from bs4 import BeautifulSoup as bs


path = "https://www.instagram.com/garageacademy.az/"


headers_parame={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0"}


request = requests.get(path,headers=headers_parame)



soup = bs(request.content,"html.parser")

test = soup.find("div",class_ = "x3nfvp2")

