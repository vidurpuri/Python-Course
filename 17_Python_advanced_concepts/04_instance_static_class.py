class Employee:
    company = "TechCorp"  # Class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def get_company(cls):
        return cls.company

    @staticmethod
    def is_working_hours(hour):
        return 9 <= hour < 17
# Example usage
if __name__ == "__main__":
    emp1 = Employee("Alice", 70000)
    emp2 = Employee("Bob", 60000)

    print(Employee.get_company())  # Output: TechCorp
    print(emp1.name)  # Output: Alice
    print(emp2.salary)  # Output: 60000
    print(Employee.is_working_hours(10))  # Output: True
    print(Employee.is_working_hours(18))  # Output: False