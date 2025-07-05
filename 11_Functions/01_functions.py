def average(a,b,c):
    d = (a + b + c) / 3
    print(d)

average(10,20,30) 


def average2(a,b,c):
    """
    Calculates the average of three numbers.

    Args:
        a (float or int): The first number.
        b (float or int): The second number.
        c (float or int): The third number.

    Returns:
        float: The average of the three input numbers.
    """
    d = (a + b + c) / 3
    return d

result = average2(10,20,30)
print(result.__doc__)