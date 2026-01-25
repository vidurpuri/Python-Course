'''
Write a decorator timer that calculates how long a function takes to execute . Test it with a function that sums numbers from 1 to 1,000,000.
'''

from time import time


def timer(func):
    def wrapper():
        start_time = time()
        func()
        end_time = time()
        print(f"Function took {end_time - start_time} seconds to execute.")
    return wrapper

@timer
def sumNumbers():
    total = 0
    for i in range(1, 1000001):
        total += i
    print(f"Sum is: {total}")
    
sumNumbers()