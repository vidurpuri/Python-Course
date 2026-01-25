# Function to sum all numbers using  *args

def sum_all(*args):
    sum = 0
    for items in args:
        sum += items
    return sum

print(sum_all(1, 2, 3, 4, 5))
