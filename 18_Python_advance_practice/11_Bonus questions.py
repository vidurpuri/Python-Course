
# combine a decorator with args and kwargs support so it can wrap any function regardless of its parameter 

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display_info(name, age):
    print("Name: {}, Age: {}".format(name, age))

@decorator_function
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 10) 
print(result)

#imlement __add__ in a Vector class so that dding two Vector objects returns a new Vector with summed components
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return "Vector({}, {})".format(self.x, self.y)
    
#call
v1 = Vector(2, 3)
v2 = Vector(5, 7)
v3 = v1 + v2
print(v3)

# Create a small program, where invalid user input raised a custom exception, logs the error and continues execution instead of crashing
class CustomError(Exception):
    pass

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

#call
get_integer_input("Enter an integer: ")