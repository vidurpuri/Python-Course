# Decorators with arguments allow you to pass parameters to the decorator function, enabling more flexible and reusable decorators.
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# In this example, the `repeat` decorator takes an argument `num_times`, which specifies how many times the decorated function should be called.
# The `greet` function is decorated with `@repeat(num_times=3)`, meaning it will print the greeting three times when called with a name.