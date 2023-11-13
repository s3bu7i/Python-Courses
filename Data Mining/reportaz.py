from bs4 import BeautifulSoup as bs
import requests

headers_parame = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0"}


request = requests.get("https://report.az", headers=headers_parame)

url = bs(request.content, "html.parser")


soup = url.find("div", class_="latest-news-container mt-2").find("div",
                                                                 class_="custom-scrollbar").find("div", class_="news-item")

print(soup)


# for x in soup:

#     print(x)

#     try:

#         link = "https://report.az" + x["href"]

#         print(link)

#     except : TypeError
