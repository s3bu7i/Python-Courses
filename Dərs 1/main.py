

a = input("Ad daxil et: ")

if a == "Aslan":
   print("Aslan emiogludru")
elif a == "Imran":
   print("Imran bibioglu")
elif a == "Islam":
   print("Isalm kursdan tanisdir")
else:
   print("Qaqa bu daxil etmemnisen ")    


password = 1234
username = "Togrul"

a = input("ad; daxil et: ")
b = int(input("Parolu daxil et: "))

if a == username and b == password:
    print("Emeliyaayt ugurla basa catdi")
elif a == username and b != password:
    print("Daxil edilen kod yalnisdir")
elif username != a:
    print("Login sehdir ")
elif password != b:
    print("Password yalnisidr")
else:
    print("Hesjazd daxil etmeidniz")

a = input("Say daxil et:")
b = input("Say daxil et:")
c = input("Say daxil et:")
 
max = max(a,b,c)
min = min(a,b,c)

print("En boyuk deyer: ", max)
print("Minumum deyer: ", min)
