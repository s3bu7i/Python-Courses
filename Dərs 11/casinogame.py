import sqlite3
import random


db = sqlite3.connect('Dərs 11/atm.db')
sql = db.cursor()

sql.execute('''
   CREATE TABLE IF NOT EXISTS users(
       id INTEGER PRIMARY KEY,
       username TEXT,
       password INTEGER,
       balance REAL
   )         
''')

sql.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        type TEXT,
        amount REAL,
        timestamp TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')

db.commit()

def register():
    username = input("Isdifadəçi adını daxil et: ")
    password = int(input("Parlolunuzu daxil edin: "))
    balance = 0.0
    
    sql.execute('INSERT INTO users (username, password, balance) VALUES (?, ?, ?)', (username, password, balance))
    db.commit()
    
    print("Qeydiyyat uğurla başa çatdı.")

def login():
    username = input("Isdifadəçi adınzı daxil edin: ")
    password = int(input("Parolunuzu daxil edin: "))
    
    sql.execute('SELECT id FROM users WHERE username = ? AND password = ?',(username, password))
    user_id = sql.fetchone()
    
    if user_id:
        print(f"Xoş gəldiniz, {username}!")
        return user_id[0]
    else:
        print("Yalnış isdifdəçi adı və ya PIN daxil etmisiniz.")
        return None

def check_balance(user_id):
    sql.execute('SELECT balance FROM users WHERE id = ?', (user_id))
    balance = sql.fetchone()[0]
    print("Sizin hesab balansınız: ${:.2f}".format(balance))

def deposit(user_id):
    amount = float(input("Daxil etmək isdədiyiniz məbləği daxil edin: "))
    sql.execute('UPDATE users SET balance = balance + ? WHERE id = ?', (amount, user_id))
    db.commit()
    print("${:.2f} hesabınıza əlavə edildi.".format(amount))
    
def withdraw(user_id):
    amount = float(input("Çıxarmaq isdədiyiniz məbləği daxil et: "))
    sql.execute('SELECT balance FROM users WHERE id = ?', (user_id))
    balance = sql.fetchone()[0]
    
    if amount > balance:
        print("Balansınızda kifayət qədər pul yoxdur. ")
        
    else:
        sql.execute('UPDATE users SET balance = balance - ? WHERE id = ?', (amount, user_id))
        db.commit()
        print("${:.2f} pul hesabınızdan çıxarıldı.".format(amount))
        
def manage_account(user_id):
    print("""
Hesab əməliyyatları:
    1. PIN kodu dəyiş
    2. Hesab məlumatları
        """)
    choice = input("Seçiminizi daxil edin: ")
    
    if choice == '1':
        new_pin = int(input("Yeni PIN kodu daxil edin: "))
    
    
def start_game(user_id):
    while True:
        print("""
Kazino oyununa xoş gəlmisiniz. Oyunun funksiyaları aşağıdakılardır:
    Oyunu başlatmaq üçün 0 düyməsinə basın :D
    1. Hesab balansınız
    2. Hesaba pul əlavə edin
    3. Hesabdan pul cıxardın
    4. Hesab əməliyyatları 
    5. Çıxış
              """)
        choice = input("Seçdiyiniz nömrəni daxil et: ")
        if choice == '1':
            check_balance(user_id)
            
    
    
start_game()


