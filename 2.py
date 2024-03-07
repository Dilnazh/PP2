import os


path = 'C:/Users/Дильназ/Desktop/Новая папка (3)/lab6(2)'

if os.path.exists(path):
    print("существует это путь")
else:
    print("нет такого")


if os.access(path, os.R_OK):
    print("читаемо")
else:
    print("не читаемо")


if os.access(path, os.W_OK):
    print("writable")
else:
    print("no writable")


if os.access(path, os.X_OK):
    print("executable")
else:
    print("no executable")