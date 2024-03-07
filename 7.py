file1 = open('C:/Users/Дильназ/Desktop/Новая папка (3)/lab6(2)/A.txt', "r")

file2 = open('C:/Users/Дильназ/Desktop/Новая папка (3)/lab6(2)/B.txt', "w")

x = file1.read()
file2.write(x)


file2.close()
file1.close()