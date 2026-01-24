from functools import reduce

a = [1,3,4,2,6,7]
# reduce takes a function and a sequence and applies the function cumulatively to the items in the sequence
# for example, if we have a list of numbers and we want to find the sum of all the numbers, we can use reduce
new = reduce(lambda x, y: x + y, a)
print(new)