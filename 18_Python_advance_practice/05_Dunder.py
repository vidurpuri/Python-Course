# Book class with dunder methods __str__ and __len__

class Book:
    def __init__  (self,title,author):
        self._title = title
        self._author = author

    def __str__(self):
        return f'{self._title} by {self._author}'
    
    def __len__(self):
        return len(self._title)
    

b = Book("1984", "George Orwell")
print(b)
print(len(b))