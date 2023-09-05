import sqlite3


db = sqlite3.connect('atm.db')

sql = db.cursor()

sql.execute(" CREATE TABLE IF NOT EXISTS atm (pin INT,cash INT) ")


pin = int(input("Pin kodu daxil edin : "))


sql.execute(f"SELECT pin FROM atm WHERE pin == '{pin}' ")

if pin in sql.fetchone():
    


    while True:

        secim = int(input(""" 
                            
        (1) Balansi yoxla\n
        (2) Kartdan Pul Cixar\n
        (3) Karta Medaxil et\n
        (4) Pini deyish\n
        (5) Cixish et"

                            
                        """))
        
        
        
        if secim == 1:
            
        
            
            sql.execute(f"SELECT cash FROM atm WHERE pin == '{pin}' ")
            
            print(sql.fetchone())

            break
        
        if secim == 2 :
            
            cash = int(input(" Meblegi daxil edin : "))
            
            sql.execute(f" UPDATE atm SET cash = cash - '{cash}' WHERE pin == '{pin}' ")
            db.commit()
            
            print('Mebleg +' +str(cash))
            
            break
        
        if secim == 3 :
            cash = int(input(" Meblegi daxil edin : "))
            
            sql.execute(f" UPDATE atm SET cash = cash + '{cash}' WHERE pin == '{pin}' ")
            
            db.commit()
            
            sql.execute(f" SELECT cash FROM atm WHERE pin = '{pin}' ")
            
            for x in sql:
                print('Umumi mebleg ' + str(x))
                
            break
        
        
        if secim == 4:
            
            pass1 = int(input(" Pini daxil edin "))
            pass2 = int(input(" Pini tesdiq edin "))
            
            if pass1 == pass2:
                
                sql.execute(f" UPDATE atm SET pin == '{pass2}' WHERE pin = '{pin}'")
                db.commit()
                print('Sizin pin Ugurla deyisdirildi')
            break
        
            
            
            
        
else:
    print('Pin yalnishdir')