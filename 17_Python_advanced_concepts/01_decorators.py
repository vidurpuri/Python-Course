# Decorators in Python
# Decorators are a powerful feature in Python that allows you to modify the behavior of a function or class method.
# They are often used to add functionality to existing code in a clean and readable way.
# A decorator is a function that takes another function as an argument, extends its behavior, and returns a new function.


def decorator(func):
    def wrapper():
        print("What is your name?")
        func()
        print("Thank you for sharing your name!")
    return wrapper


@decorator
def display_name():
    print("Vidur Puri")
# The above code defines a decorator that adds functionality before and after the execution of the display_name function.
# The decorator prompts the user for their name, calls the display_name function, and then thanks the user for sharing their name.
# The @decorator syntax is a shorthand for applying the decorator to the function.
display_name()


# Applying the decorator to the display_name function
f = decorator(display_name)
f()