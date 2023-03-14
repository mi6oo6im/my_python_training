from typing import List


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book(self, book_title: str):
        try:
            book = next(filter(lambda b: b.title == book_title, self.books))
        except StopIteration:
            return 'This book is not in the library'
        return book


b1 = Book('101 dalmatians', 'Dodie Smith')
b2 = Book('1001 nights', 'Unknown')

library = Library()
library.add_book(b1)
library.add_book(b2)

