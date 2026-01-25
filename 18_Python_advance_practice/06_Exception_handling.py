# Define custom exception for negative numbers 

class NegativeNumberError(Exception):
    pass

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    if a < 0 or b < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    result = a / b
    print(result)
except ValueError:
    print("Invalid input. Please enter numbers only.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except NegativeNumberError as e:
    print("Error:", e)
