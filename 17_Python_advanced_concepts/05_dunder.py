# Dunder Methods in Python
# Dunder methods, also known as magic methods or special methods, are a set of predefined methods in Python that allow you to define 
# the behavior of your objects for built-in operations. They are named with double underscores before and after the method name 
# (hence "dunder").
# Common dunder methods include:
# - `__init__(self, ...)`: Constructor method, called when an object is created
# - `__str__(self)`: Defines the string representation of an object, used by the `print()` function
# - `__repr__(self)`: Defines the official string representation of an object, used
#   by the `repr()` function
# - `__len__(self)`: Defines the behavior of the built-in `len()`   
#   function for the object
# - `__getitem__(self, key)`: Defines the behavior of indexing (e.g., `obj[key]`)
# - `__setitem__(self, key, value)`: Defines the behavior of item assignment (e.g., `obj[key] = value`)
# - `__delitem__(self, key)`: Defines the behavior of item deletion (                           e.g., `del obj[key]`)
# - `__iter__(self)`: Returns an iterator object for the object, allowing it    


#   to be iterable (e.g., in a `for` loop)
# - `__next__(self)`: Returns the next item from the iterator       
# - `__contains__(self, item)`: Defines the behavior of the `in` operator (e.g., `item in obj`)
# - `__call__(self, ...)`: Allows an object to be called as a function
# - `__eq__(self, other)`: Defines the behavior of the equality operator (`==`)
# - `__ne__(self, other)`: Defines the behavior of the inequality operator (`!=`)
# - `__lt__(self, other)`: Defines the behavior of the less than operator   
#   (`<`)
# - `__le__(self, other)`: Defines the behavior of the less than or equal to operator (`<=`)
# - `__gt__(self, other)`: Defines the behavior of the greater than operator (`>`)
# - `__ge__(self, other)`: Defines the behavior of the greater than or equal to operator (`>=`)
# - `__hash__(self)`: Defines the behavior of the built-in `hash()` function for the object
# - `__bool__(self)`: Defines the behavior of the built-in `bool()` function for the object
# - `__enter__(self)`: Defines the behavior of entering a context (used in `with` statements)
# - `__exit__(self, exc_type, exc_value, traceback)`: Defines the behavior of exiting a context (used in `with` statements)
# - `__del__(self)`: Destructor method, called when an object is about to be destroyed
# - `__getattr__(self, name)`: Called when an attribute is accessed that does not exist
# - `__setattr__(self, name, value)`: Called when an attribute is set
# - `__delattr__(self, name)`: Called when an attribute is deleted
# - `__format__(self, format_spec)`: Defines the behavior of the built-in `format()` function for the object
# - `__sizeof__(self)`: Returns the size of the object in bytes

# Example of using dunder methods in a custom class:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Vector(self.x / scalar, self.y / scalar)
        return NotImplemented
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented
    def __len__(self):
        return 2
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Index out of range")
    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Index out of range")
    def __delitem__(self, index):
        if index == 0:
            self.x = 0
        elif index == 1:
            self.y = 0
        else:
            raise IndexError("Index out of range")  # noqa: E701