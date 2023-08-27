#Funksiyalar

def rectangle_area(length, width):
    area = length*width
    return area

length = float(input("Uzunluğu daxil et: "))
width = float(input("Enini daxil et: "))

result = rectangle_area(length, width)

print(f"Dairənin sahəsi: ",result)
