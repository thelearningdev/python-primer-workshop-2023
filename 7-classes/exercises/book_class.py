"""
1. Create a Book class with attributes title, author, publisher, genre, and price.

2. Add a method to the Book class called discount that takes a percentage as an argument and returns the discounted price of the book.

3. Create an instance of the Book class and test the discount method.


4. Create a Fiction subclass of Book that adds an attribute called plot and a method called print_plot that prints the plot of the book.

5. Create an instance of the Fiction class and test the print_plot method.

6. Create a NonFiction subclass of Book that adds an attribute called topic and a method called print_topic that prints the topic of the book.

7. Create an instance of the NonFiction class and test the print_topic method.
"""
class Book:
    """
    attributes: title, author, publisher, price
    method: discount
    """
    def discount(self, percentage):
        pass

class FictionBook(Book):
    pass
    # plot
    # get_plot

class NonFiction(Book):
    pass
    # topic
    # get_topic

# Create instance of book class with discount method


# if done, try the ones left from `5-collection-data-types`

1. Finish off the book class
2. Finish 5-collection-data-types/exercises/1_exercises.py
3. Combine 1 & 2, with class BookShelf, get_book, remove_book, reorder_book_by_date, reorder_book_by_pages