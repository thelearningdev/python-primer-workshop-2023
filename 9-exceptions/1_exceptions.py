try:
    # some code that may raise exceptions
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
    print(z)
except ValueError:
    print("Invalid input. Please enter only numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
    
except NameError:
    print("Name erorr occured")
finally:
    print("This code will always be executed.")
