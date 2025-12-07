class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        print(f"Deleting {self.title}")


class Library:
    def __init__(self):
        self._books = []  # private list of Book objects

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False  # book not found

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False  # book not found

    def list_available_books(self):
        """Print all books that are not checked out."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")




