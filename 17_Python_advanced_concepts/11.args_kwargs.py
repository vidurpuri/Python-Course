#explain args and kwargs in python
'''
In Python, *args and **kwargs are used to pass a variable number of arguments to a function.

*args allows you to pass a variable number of non-keyword arguments to a function. It is represented by an asterisk (*) followed by the variable name. 
Inside the function, *args is treated as a tuple of the positional arguments passed to the function.



'''
def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)
my_function('a', 'b', 'c')

'''
**kwargs allows you to pass a variable number of keyword arguments to a function. It is represented by two asterisks (**) followed by the variable name. 
Inside the function, **kwargs is treated as a dictionary of the keyword arguments passed to the function.
'''


def my_function(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

my_function(a=1, b=2, c=3)
my_function(name='Alice', age=30)

#In summary, *args is used for non-keyword arguments, while **kwargs is used for keyword arguments. They provide a flexible way to pass arguments to functions in Python.
