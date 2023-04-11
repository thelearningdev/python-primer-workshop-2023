# Creating a file object

f = open("data/books.csv", "r")


# Reading a file

print (f.read())


# Writing to a File

f = open("data/new.txt", "w")
f.write("A new file is created an new data is entered")
f.close()

# Appending data to a file

f = open("data/new.txt", "a")
f.write("A new file is created an new data is entered")
f.close()

# File seek

f = open("data/books.csv", "r")
print (f.read())
print (f.read()) # what's happening here

f.seek(0)
print (f.read())