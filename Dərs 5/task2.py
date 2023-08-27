#Boş olan indexləri çıxıb listi yenidən çap etmək 

test_list = [5,6,[],3,[],[],9]

non_empty_item = [item for item in test_list if item != []]

for element in non_empty_item:
    print(element)

