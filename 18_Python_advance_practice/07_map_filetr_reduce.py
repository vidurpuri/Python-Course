from functools import reduce

# Use map() to convert numbers to their cubes

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * x * x, numbers))
print("Using map to cube each number:", result)

# Use filter() to get even numbers

num = [10,11,12,13,14]
filterResult = list(filter(lambda x: x %2 ==0, num))
print("Using filter to get even numbers:", filterResult)


# Use reduce() to get products of all numbers 

data = [1, 2, 3, 4]
reducedResult = reduce(lambda x, y: x * y, data)
print("Using reduce to multiply all numbers:", reducedResult)