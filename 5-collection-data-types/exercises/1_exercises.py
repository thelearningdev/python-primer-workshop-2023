def read_books():
    with open("data/books.csv") as f:
        return f.read()

def convert_data_to_list_of_list(data):
    # data is a string
    list_of_books = []

    # fill this function to convert data into list of lists

    # split the data into lines # refer split function under string
    # for each line # for loop
    # split them by comma # refer split function under string
    # add that list to list_of_books # refer append function in list
    # Return list_of_books

    print(list_of_books)
    # output should look like this
    # [
    #     ["the great gatsby", "scott fitzgerald",1925],
    #     ["to kill a mockingbird","harper lee",1960],
    # ]

def get_list_of_dict(data):
    list_of_dict = []

    """
    [
        {"Book Name":"the great gatsby", "author": "scott fitzgerald", "year": 1925 }
        {"Book Name":"the great gatsby", "author": "scott fitzgerald", "year": 1925 }
        {"Book Name":"the great gatsby", "author": "scott fitzgerald", "year": 1925 }
        {"Book Name":"the great gatsby", "author": "scott fitzgerald", "year": 1925 }
    ]
    """

    list_of_dict = []

    for x in data.split("\n"):
        # x will look like `the great gatsby,scott fitzgerald,1925`
        # y = x.split() `["the great gatsby", "scott fitzgerald",1925]`
        # y[0] y[1] y[2] to construct a new dict
        # append the new dict to the list
        pass

    return list_of_dict

data = read_books()
print(type(data), data)
convert_data_to_list_of_list(data)


# list_of_list = convert_data_to_list_of_list(data)
# print(list_of_list)


## 2. Write a funtion `filter_data` that prints all the books writtern before 1800


## 3. Will the same function work for 1990


## 4. Update the same function to work with a range eg., 1700 to 1800.


## 5. Write a function that returns a dict with author name as key and the books they published as values

# author_books = get_book_by_author(data)
# sample_output = {
#     "jane austen": [
#         {"name": "Pride and Prejuidice", "year": 1813},
#         {"name": "Sense and Sensibility", "year": 1811},
#     ],
#     "george orwell": [{
#         {"name": "animal farm", "year": 1945},
#     }]
# }
