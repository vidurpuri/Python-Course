# Employee class with getter and setter for salary

class Employee:
    def __init__(self,salary):
        self._salary = salary # protected attribute
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if(value < 0):
            print("Invalid salary. Salary must be positive.")
        else:
            self._salary = value

e = Employee(50000)
print(e.salary)
e.salary = 60000
print(e.salary)
e.salary = -10000
