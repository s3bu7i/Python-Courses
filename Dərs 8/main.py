import time
from datetime import datetime

def calculate_age(birth_day):
    today = datetime.now()
    age = today - birth_day
    years = age.days //365 
    month = (age.days%365)/30
    days = age.days%30
    hours, reminder = divmod(age.seconds, 3600)
    minutes, seconds = divmod(reminder, 60)
    return years,month, days, hours, minutes, seconds

birt_date = input("Doğum tarixinizi qeyd edin(gün/ay/il): ")
birth = datetime.strptime(birt_date, "%d/%m/%Y")

years, month, days, hours, minutes, seconds = calculate_age(birth)

print(f"Sizin yaşınız {years} il {month} ay {days} gün {hours} saat {minutes} dəqiqə {seconds} saniyə yaşındasınız")


