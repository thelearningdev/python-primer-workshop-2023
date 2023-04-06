# Run this code

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


# Equivalent code with if...else

def switch(lang):
    if lang == "JavaScript":
        return "You can become a web developer."
    elif lang == "PHP":
        return "You can become a backend developer."
    elif lang == "Python":
        return "You can become a Data Scientist"
    elif lang == "Solidity":
        return "You can become a Blockchain developer."
    elif lang == "Java":
        return "You can become a mobile app developer"

print(switch("JavaScript"))   
print(switch("PHP"))   
print(switch("Java"))  
