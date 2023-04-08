# Make the following snippet data driven

# Hint: Using a python data type to store the data and then retrive it dynamically based on input


lang = input("What's the programming language you want to learn? ")

lang = lang.lower()

match lang:
    case "javaScript":
        print("You can become a web developer.")

    case "python":
        print("You can become a Data Scientist")

    case "php":
        print("You can become a backend developer")
    
    case "solidity":
        print("You can become a Blockchain developer")

    case "java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")

