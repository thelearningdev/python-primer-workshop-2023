import requests

# Mock API dashboard - https://beeceptor.com/console/python-primer

URL = "https://raw.githubusercontent.com/HariVM/Analytics/master/1000%20Sales%20Records.csv"

# Use request library to get data from this URL
# Write it to a sales.csv file


URL = "https://python-primer.free.beeceptor.com/book"

# Create  Post request to the above API with following data

data = {
    "author": "Chinua Achebe",
    "country": "Nigeria",
    "imageLink": "images/things-fall-apart.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Things_Fall_Apart\n",
    "pages": 209,
    "title": "Things Fall Apart",
    "year": 1958
}


# Create GET request to the above API with following data