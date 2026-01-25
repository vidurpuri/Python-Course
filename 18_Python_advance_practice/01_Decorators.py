'''
Write a decorator that prints " Function is called" before the function runs . Use it to decorate a function say_hello() that prints " Hello !"
'''
def logger(func):
    def wrapper():
        print('Function is being Called')
        func()
    return wrapper


@logger
def say_hello():
    print('Hello !')

say_hello()
