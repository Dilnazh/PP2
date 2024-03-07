import os

path = "C:/Users/Дильназ/Desktop/Новая папка (3)/lab6(2)/text.txt"

count = 0

file = open(path, 'r')
for x in file:
    count += 1

file.close()

print("Total number of lines:", count)