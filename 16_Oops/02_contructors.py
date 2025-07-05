class Employee:
    def __init__(self, name, age, salary):
        self.name = name 
        self.age = age 
        self.salary = salary

    def get_Sal(self): #Self is a reference to the current instance of the class
        return self.salary
    
E1 = Employee("Vidur", 31, 100000)
print(E1.get_Sal())
E2 = Employee("Amit", 30, 200000)
print(E2.get_Sal())

#object Introspection
print(dir(E1))  # Lists all attributes and methods of the object
print(E1.__dict__)  # Prints the __dict__ attribute, which contains the object's
