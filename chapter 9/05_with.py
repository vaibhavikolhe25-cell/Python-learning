f = open("file.txt")
print(f.read())
f.close()

# the same can be written using the statement like this
with open("file.txt") as f:
    print(f.read())

# you dont have to explicitly close the File
