from bs4 import BeautifulSoup as bs
import requests
import sqlite3

db = sqlite3.connect("news.db")

sql = db.cursor()

sql.execute("""
            
            CREATE TABLE  IF NOT EXISTS news (
                
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category VARCHAR(50) ,
                date VARCHAR(50),
                title VARCHAR(200),
                text TEXT,
                img TEXT,
                weather VARCHAR(70)
                
                )
            
            
            """)




data = requests.get("https://lent.az")

url = bs(data.text,"html.parser")

soup = url.find("div",class_ = "all-news-wrapper")

for x in soup:
    
    
    try:
        
        link = x["href"]
        
        data1 = requests.get(link)
        soup1 = bs(data1.text,"html.parser")
        
        category = soup1.find("div",class_ = "breadcrumb_row").text
        
        date = soup1.find("div",class_ = "overlay").text.replace("(UTC +04:00)","")
        
        
        title = soup1.find("h1",class_ = "news_title").text
        
        text = soup1.find("div",class_ = "news_content").find("p").text
        
        
        
        image = soup1.find("div",class_ = "news_img").find("img")
        
        
        weather = soup1.find("div",class_ = "top_section").find_all("li")[3].text
    
        
        sql.execute(f"""
                    
                    INSERT INTO news (category,date,title,text,img,weather) 
                    
                    VALUES('{category}','{date}','{title}','{text}','{image}','{weather}')
                    
                    """)
        
        db.commit()
        
        
    except:TypeError


