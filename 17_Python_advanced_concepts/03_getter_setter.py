class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Using a single underscore to indicate a protected attribute
    @property
    def first_name(self):
        return self.name.split(" ")[0]
    
    @first_name.setter
    def first_name(self, updatedFirstName):
        f = self.name.split(" ")
        f[0] = updatedFirstName
        self.name = " ".join(f)

e = Employee("John Doe", 50000)
print(e.first_name)  # Output: John
e.first_name = "Jane"
print(e.name)  # Output: Jane

# Behind the scene implementation without settter abnd getter
# print(e.first_name())  # Output: John
# e.set_first_name("Jane")
# print(e.name())  # Output: Jane Doe
