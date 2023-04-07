"""
Define a Book class with the following attributes:

title (string)
author (string)
year (integer)
pages (integer)

Define a book_list class that can hold book objects



"""


class Book:
    pass


class BookList:
    pass


book_list = BookList()
book_1 = Book("book1", "author1", 2023, 380)
book_2 = Book("book2", "author2", 1993, 440)
book_3 = Book("book3", "author3", 1893, 990)


book_list.append(book_1)
book_list.extend([book_2, book_3])

book_list.sort()
len(book_list)

print (book_1 > book_2) # should return True based on the year
