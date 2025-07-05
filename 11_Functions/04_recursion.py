# Explain solution of fibonacci series using recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# Example usage
n = 10
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
# The Fibonacci series is a sequence where each number is the sum of the two preceding ones, usually starting with 0 and 1.
# The series goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# The function `fibonacci` uses recursion to calculate the nth Fibonacci number:    
# 1. If `n` is less than or equal to 0, it returns 0.
# 2. If `n` is 1, it returns 1.
# 3. For all other values of `n`, it returns the sum of the two preceding Fibonacci numbers.
# This is done by calling the `fibonacci` function with `n - 1` and `n - 2`, effectively breaking down the problem into smaller subproblems until it reaches the base cases.
# This recursive approach is elegant but can be inefficient for large `n` due to repeated calculations.
# For larger values of `n`, an iterative approach or memoization can be used to improve performance.

