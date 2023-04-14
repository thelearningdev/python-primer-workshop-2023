class CustomException(Exception):
    pass


try:
    # Some code that may raise the CustomException
    raise CustomException("This is a custom exception")
    # 1 / 0
except CustomException as e:
    # Handle the exception here
    print("Caught CustomException:", e)


# ------------------------------------

import requests


class APIException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message


try:
    response = requests.get("https://api.example.com/data")
    if response.status_code != 200:
        raise APIException(response.status_code, "API returned an error")
except APIException as e:
    print(f"API Error: {e.status_code} - {e.message}")

# You can also reraise a exception that's caught
