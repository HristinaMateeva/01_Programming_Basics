class Book:
    def __init__(self, content, title, author):
        self.content = content
        self.title = title
        self.author = author


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class PrePrintFlayer:
    def format(self, book):
        return f"----------\n{book.title}\n----------\n{book.author}\n----------"


class Printer:
    def __init__(self, formatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        return self.formatter.format(book)
