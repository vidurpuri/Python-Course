# List comprehension to add table of 5 in list
table_of_5 = [5 * i for i in range(1, 11)]

# Simple method of Sqrt
sqrt = []

for i in range(5):
    sqrt.append(i**2)

print(sqrt)

# Comprehension Method of Sqrt 

sqrt_LC = [i**2 for i in range(5)]
print(sqrt_LC)