# Class is a blueprint for creating objects. Objects are instances of classes.
# Class encapsulates data for the object and methods to manipulate that data.

class Employee:
    name = "Vidur"
    age = 31
    company = "NAB"

    def get_Sal(self): #Self is a reference to the current instance of the class
        return 100000
    
# Creating an instance of the Employee class
emp1 = Employee()
# Accessing attributes and methods of the instance
print(emp1.name)        # Output: Vidur 

print(emp1.get_Sal())  # Output: 100000