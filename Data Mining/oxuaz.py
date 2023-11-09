import requests
from bs4 import BeautifulSoup as bs

path = "https://oxu.az"


headers_parame={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0"}


request = requests.get(path,headers=headers_parame)



soup = bs(request.content,"html.parser")

# print(soup)

# category = soup.find_all("a",class_="nav-i")[5].text

category1 = soup.find("nav",class_ = "nav").find_all("a",{"class":"nav-i"})
# category2 = soup.find("nav",class_ = "nav").find("a",{"class":"nav-i"}).find_next_sibling()


# print(category1)


