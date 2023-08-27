#tuple data tipinə bir element əlavə et

my_tuple = ("Apple", "Banana", "Oragne")

new_element = 66
list_version = list(my_tuple)
list_version.append(new_element)
new_tuple = tuple(list_version)

result_tuple = my_tuple + (new_element,)

print(new_tuple)
print(result_tuple)



