class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Bark")

class Cat(Animal):
    def speak(self):
        super().speak()
        print("Meow")

# Creating instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")
# Calling the speak method on each instance
dog.speak()  # Output: Animal sound Bark
cat.speak()  # Output: Animal sound Meow
