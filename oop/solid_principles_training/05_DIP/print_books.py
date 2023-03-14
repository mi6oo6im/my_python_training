from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class IFormatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        return book.content


class Formatter(IFormatter):
    def format(self, book: Book) -> str:
        return book.content


class IPrinter(ABC):
    @abstractmethod
    def get_book(self, book: Book):
        pass


class Printer(IPrinter):
    def __init__(self, formatter: IFormatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        formatted_book = self.formatter.format(book)
        return formatted_book


book = Book('Some book')
formatter = Formatter()
printer = Printer(formatter)

formatted_book = printer.get_book(book)
print(formatted_book)
