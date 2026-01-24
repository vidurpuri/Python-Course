a = [1,2,3,4,5,6,7,8,9];

def square(x):
    return x * x;

new = list(map(square,a)); # we need to convert to list() because by default this map object which needs further conversion to list or we can iterate a s well 
print(new);