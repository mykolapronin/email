import pytest
from homework_library import Book, Library


@pytest.fixture(scope="class")
def library_fixture():
    library = Library()
    book1 = Book("АДВЛТОЬО", "МихайлоМ удрик")
    book2 = Book("1988", "Джордж Оел")
    library.add_book(book1)
    library.add_book(book2)
    return library


class TestLibrary:
    def test_list_books(self, library_fixture):
        expected_books = [
            '"АДВЛТОЬО" by МихайлоМ удрик',
            '"1988" by Джордж Оел'
        ]
        assert library_fixture.list_books() == expected_books

    def test_add_book(self, library_fixture):
        new_book = Book("Фауст", "Гете")
        library_fixture.add_book(new_book)
        assert '"Фауст" by Гете' in library_fixture.list_books()

    def test_remove_book(self, library_fixture):
        book_to_remove = Book("1988", "Джордж Оел")
        library_fixture.remove_book(book_to_remove)
        assert '"1988" by Джордж Оел' not in library_fixture.list_books()

    def test_remove_nonexistent_book(self, library_fixture):
        nonexistent_book = Book("Привид у броні", "Микола Пронін")
        with pytest.raises(ValueError):
            library_fixture.remove_book(nonexistent_book)
