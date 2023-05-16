from typing import List

class Taggable:
    def tag(self) -> List[str]:
        pass

class Book(Taggable):
    __id_count = 0
    
    def __init__(self, author: str, title: str):
        if not title:
            raise ValueError("Title can't be empty.")
        self.author = author
        self.title = title
        self.__id = Book.__id_count
        Book.__id_count += 1
        
    def __str__(self):
        return f"[{self.__id}] {self.author} '{self.title}'"
    
    def tag(self):
        return [word for word in self.title.split() if word.istitle()]

class Library:
    def __init__(self, number: int, address: str):
        self.number = number
        self.address = address
        self.books = []
        
    def __iadd__(self, book: Book):
        self.add_book(book)
        return self
        
    def add_book(self, book: Book):
        self.books.append(book)
        
    def __iter__(self):
        return iter(self.books)

# пример использования
lib = Library(1, "51 Some str., NY")
lib += Book("Leo Tolstoi", "War and Peace")
lib += Book("Charles Dickens", "David Copperfield")

for book in lib:
    print(book)
    print(book.tag())