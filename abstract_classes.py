from abc import ABC, abstractmethod


class LibraryItem(ABC):

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    @abstractmethod
    def description(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class Book(LibraryItem):
    def __init__(self, number_of_pages: int, title: str, author: str, year: int):
        super().__init__(title, author, year)
        self.number_of_pages = number_of_pages

    def description(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Pages: {self.number_of_pages}"


class Magazine(LibraryItem):
    def __init__(self, issue_number: int, title: str, author: str, year: int):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def description(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Issue_number: {self.issue_number}"


class DVD(LibraryItem):
    def __init__(self, duration: int, title: str, author: str, year: int):
        super().__init__(title, author, year)
        self.duration = duration

    def description(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Duration: {self.duration}"


libre = Book(174, "Elden Ring", 'Miyadzaki', 2014)
libre1 = Magazine(20, "Playboy", 'Eichiro Oda', 1997)
libre2 = DVD(200, "The Boys", 'Oleksii Durov', 2007)

print(Book.description(libre))
print(Magazine.description(libre1))
print(DVD.description(libre2))

