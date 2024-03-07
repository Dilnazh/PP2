my_list = ["Dari", "Anel", "Nazek", "Dil","Aiz"]

# Открываем файл для добавления списка
file = open("C:/Users/Дильназ/Desktop/Новая папка (3)/lab6(2)/text.txt", "a")
file.write(str(my_list))
file.close()


f = open("C:/Users/Дильназ/Desktop/Новая папка (3)/lab6(2)/text.txt", "r")
print(f.read())