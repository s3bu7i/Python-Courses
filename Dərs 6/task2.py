#bir dictionary verilib 
#bir input olsun və 1 və 2 dəyərləri olsun
#1 ə basdıqda dict də keysləri versin
#2 ə basdıqda dict dəki valueləri yazdırsın
#ad daxil etməyəndə error versin ad daxil etmədiniz yazsın

my_dict = {
    "Model":"Ford",
    "İli":2004,
    "Kompanya":"Mustang"
}

print("""
Bir ədəd seç:
1 - Mövcud keysləri göstərmək
2 - Mövcud dəyərləri verir
""")
a = int(input("Bir ədəd daxil et : "))

if a == 1:
    keys = my_dict.keys()
    print("Keyslər - ",keys)
elif a ==2:
    values = my_dict.values()
    print("Dəyərlər - ",values)
else:
    print("Bir məlumat daxil edin :D")

