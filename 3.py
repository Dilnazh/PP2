import os

path = 'C:/Users/Дильназ/Desktop/Новая папка (3)/lab6(2)'


if os.path.exists(path):
    print("exists")
    
    
    directory, filename = os.path.split(path)
    
    print("Directory:", directory)
    print("Filename:", filename)
    
else:
    print("not exist")