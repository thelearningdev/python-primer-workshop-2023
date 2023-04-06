import sqlite3

def connect_to_database(database_name):
    
    # Inner function 1
    def inner_function(func):

        # Inner function 2
        def wrapper(*args, **kwargs):
            with sqlite3.connect(database_name) as conn:
                cursor = conn.cursor()
                result = func(cursor, *args, **kwargs)
                conn.commit()
                return result
        return wrapper

    return inner_function

@connect_to_database('books.db')
def create_book_table(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER)")

@connect_to_database('books.db')
def insert_books(cursor, books):
    cursor.executemany("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", books)

@connect_to_database('books.db')
def select_all_books(cursor):
    cursor.execute("SELECT * FROM books")
    return cursor.fetchall()


# Create the 'books' table
create_book_table()

# Insert some books
books = [
    ("Pride and Prejudice", "Jane Austen", 1813),
    ("To Kill a Mockingbird", "Harper Lee", 1960),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925)
]
insert_books(books)

# Retrieve all books
all_books = select_all_books()
print(all_books)
