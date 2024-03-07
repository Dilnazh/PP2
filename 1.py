import os

path = 'C:/Users/Дильназ/Desktop/Новая папка (3)/lab6(2)'
print("директория:")
for x   in os.listdir(path):
    if os.path.isdir(os.path.join(path, x)):
        print(x)
print("\nФайлы:")
for x in os.listdir(path):
    if os.path.isfile(os.path.join(path, x)):
        print(x)
        
print("\nСпециальная дорожка:")
for root, dirs, files in os.walk(path):
    for dir in dirs:
        print(os.path.join(root, dir))
    for file in files:
        print(os.path.join(root, file))