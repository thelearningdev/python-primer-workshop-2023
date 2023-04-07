# HTTP methods

import requests

headers={"Accept": "application/json"}
response = requests.get("https://icanhazdadjoke.com/", headers=headers)
response = response.json()

# Print response and see how it looks?
# What's it's data type
# extract only the joke from it