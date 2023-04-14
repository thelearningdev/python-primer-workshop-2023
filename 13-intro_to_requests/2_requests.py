# HTTP methods

import requests

headers={"Accept": "application/json"}
response = requests.get("https://icanhazdadjoke.com/", headers=headers)
response = response.json()
# dict
# {"id":"7E69M792Tvc","joke":"I've got a joke about vegetables for you... but it's a bit corny.","status":200}
print (response)

# Print response and see how it looks?
# What's it's data type
# extract only the joke from it





# REST APIs
# BASE_URL = "http://bhavanibook.com/"
# GET - Read data  - book/10 - returns the book with id or returns an error BookNotFound
# PUT - Update an existing - book/10 - {"name": "newbook"} - {status}
# POST - Create something new - book/ - {"name": "newbook"} - {status, id}
# DELETE - delete an item - book/10 - {status}
# List(GET) - book/ - - 
# {"status": "success", 
# "data": [{"name": "newbook", id:1}, {"name": "newbook", id:2}, {"name": "newbook", id:3}]}