"""
This script demonstrates basic tuple operations in Python:
- Defining tuples, including single-element tuples.
- Tuple unpacking: assigning tuple elements to variables.
- Common tuple methods:
    - count(): Counts the number of occurrences of a specified element.
    - index(): Returns the index of the first occurrence of a specified element.
"""

# How to define tuple
t = (2,4,6,8)

# How to define tuple with single element
t1 = (5,)

# Tuple Unpacking

t2 = (3,6,8,9)

a,b,c,d = t2
print(a,b,c,d)

#common methods of tuples
t2.count(3) # count the no. of occurence of element in tuple 
t2.index(3) # provide the index of mentioned element in tuple 

