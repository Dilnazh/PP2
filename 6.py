import string

alphabet = string.ascii_uppercase

for x in alphabet:
    filename = x + ".txt"
    file = open(filename, "w")
    file.write("This is file " + filename)