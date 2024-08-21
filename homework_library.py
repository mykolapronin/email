class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'"{self.title}" by {self.author}'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for existing_book in self.books:
            if existing_book.title == book.title and existing_book.author == book.author:
                self.books.remove(existing_book)
                return
        raise ValueError("No books found")

    def list_books(self):
        return [str(book) for book in self.books]
