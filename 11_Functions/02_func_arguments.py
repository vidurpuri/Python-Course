#positional arguments
def greet(name, greeting):
    print(f"{greeting}, {name}!")

greet("Alice", "Hello")

#default arguments
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")

#keyword arguments
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet( greeting="Hi", name="Alice")