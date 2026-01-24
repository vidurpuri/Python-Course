a = [1,2,3,4,5,6,7,8,9]

def is_greater_than_5(x):
    if x > 5:
        return True
    else:
        return False
    

new = list(filter(is_greater_than_5, a))
print(new)