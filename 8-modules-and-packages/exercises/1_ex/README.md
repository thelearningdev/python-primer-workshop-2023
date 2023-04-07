# Exercise

## Create a Custom module book.py under bookstore folder

1. Create a Book class with the following attributes:

```
title (string)
author (string)
genre (string)
price (float)

Functions:
to_dict: returns the attributes as a dict
```

## Create a Custom module bookstore.py under bookstore folder

2. Create a Bookstore class with the following attributes:

```
books (list of Book objects)

Functions:


add_book(book): adds a book to the list of books
remove_book(book): removes a book from the list of books
search_book(title): searches for a book in the list of books by title and returns the book object if found, otherwise returns None.
to_csv(path): saves the list of books as csv to the path
to_dict(): return a dict of list {"books": [{....}, {....}]}
```

## Create book_app.py

1. Create a Bookstore object
2. Creates several Book objects and adds them to the Bookstore object (use the csv file from previous exercise)
3. Searches for a book by title
4. Removes a book from the Bookstore object
5. Prints out the remaining books in the Bookstore object
