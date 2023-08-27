
#bedenn kutle indexi yoxalayan

# İstifadəçidən boy və kilo dəyərlərini alırıq
boy = float(input("Boyunuzu (metr) daxil edin: "))   
kilo = float(input("Kilonuzu daxil edin: "))

# Beden Kitle İndeksini hesablayırıq
bki = kilo / (boy * boy)

# Beden Kitle İndeksini değerlendirir və uyğun mesajı çap edirik
if bki < 18.5:
    print("Beden Kitle İndeksi:", bki)
    print("Zeyif")
elif 18.5 <= bki < 25:
    print("Beden Kitle İndeksi:", bki)
    print("Normal kilo")
elif 25 <= bki < 30:
    print("Beden Kitle İndeksi:", bki)
    print("yeke kilolusunuz")
else:
    print("Beden Kitle İndeksi:", bki)
    print("obez")

#2 while vasitesile 1 -den 10-a qeder ededlerin vurma cedvelini ekrana cixart

row = 1
while row <= 10:
    column = 1
    while column <= 10:
        result = row * column
        print(f"{row} * {column} = {result}\t", end="")
        column += 1
    print()
    row += 1

