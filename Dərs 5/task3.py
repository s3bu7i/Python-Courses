#Bir ədəd listimiz var və adlar verilib
#bir input var və 2 seçim soruşur: 1 ə basdıqda ad daxil etmək üçün input açılsın, 2 yə basdıqda soruşsun silməy isdədiyinz adı daxil edin
#error mesajı kimi ad daxil etməyəndə və ad limiti 15 i keçdikdə error versin 

my_list = ["Mary","Jhon","Sara","Tony","Jane"]

print("""
    Seçiminiz edin:
        1 - Listə ad əlavə etmək
        2 - Listdən daxil edilən ədədin silinməsi
""")

a = int(input("Daxil etdiyiniz nömrəni yazın: "))

if a == 1:
    name = str(input("Daxil etmək isdədyiniz adı yazlın: "))
    my_list.append(name)
    print(my_list)
elif a == 2:
    delname = str(input("Silmək isdədyiniz adı daxil edin: "))
    while delname in my_list:
        my_list.remove(delname)
    print(my_list)


