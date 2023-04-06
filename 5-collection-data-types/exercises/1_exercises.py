def read_books():
    with open("data/books.txt") as f:
        return f.read()


def convert_data_to_list_of_list(data):
    list_of_books = None

    # fill this function to convert data into list of lists

    print(list_of_books)


def convert_data_to_list_of_dict(data):
    list_of_books = None

    # fill this function to convert data into list of lists

    print(list_of_books)


data = read_book()
print(data)


list_of_list = convert_data_to_list_of_list(data)
print(list_of_list)


## 2. Write a funtion `filter_data` that prints all the books writtern before 1800


## 3. Will the same function work for 1990


## 4. Update the same function to work with a range eg., 1700 to 1800.


## 5. Write a function that returns a dict with author name as key and the books they published as values

author_books = get_book_by_author(data)
# sample_output = {
#     "jane austen": [
#         {"name": "Pride and Prejuidice", "year": 1813},
#         {"name": "Sense and Sensibility", "year": 1811},
#     ],
#     "george orwell": [{
#         {"name": "animal farm", "year": 1945},
#     }]
# }
