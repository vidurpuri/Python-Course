# Description: A utility class for basic math operations stating functionality of static and class method defination and how they are called 

class MathUtils:

    def __init__(self):
        pass

    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def description(cls):
        print('This is a utility class for math operations')

# Create an instance of MathUtils
m = MathUtils()
m.description()
print(m.add(5, 10))


# Call functions without creating objects
print(MathUtils.add(2,4))
MathUtils.description()

