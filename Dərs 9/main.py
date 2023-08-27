import os
import time

def specific_element_writer():
    specific_elements = input("Daxil etmək isdədiyinz məlumatları yaz: ")
    with open("./Dərs 9/main.txt", "a") as file:
        for element in specific_elements:
            #file.write(element + "\n")
            file.write(element)
            print(f"{element} fayla yazdırıldı")
        
def file_remove():
    try:
        os.remove("./Dərs 9/main.txt")
        print("main.txt faylı uğurla silindi")
    except FileNotFoundError:
        print("main.txt faylı tapılmadı")
def file_read(file_name):
    try:
        with open(file_name, "r") as file:
            text = file.read()
            print(text)
    except FileNotFoundError:
        print(f"{file_name} faylı tapmaq olmadı")
    except Exception as e:
        print(f"Faylı oxunma zamanı bir xəta baş verdi: {e}")

while True:
    print("""
    Bir seçim et: 
    1 - Spesifik element yazdır
    2 - Mövcud faylı sil
    3 - Faylı tam oxu
    """)
    a = int(input("Seçdiyiniz nömrəni daxil et: "))
    if a == 1:
        specific_element_writer()
    elif a == 2:
        file_remove()
    elif a == 3:
        #file_name = input("Oxumaq isdədiyinz faylın adın daxil edin: ")
        file_name = "./Dərs 9/main.txt"
        file_read(file_name)
    else:
        print("Daxil etdiyinz nömrədə səhvlik var, yenidən cəhd edin")
    time.sleep(3)
    
    


