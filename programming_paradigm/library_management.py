# library_management.py

class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author):
        """Initialize a book with title, author, and availability."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute for encapsulation

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Already checked out

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # Already available

    def is_available(self):
        """Return True if the book is available."""
        return not self._is_checked_out


class Library:
    """A class representing a library that manages a collection of books."""

    def __init__(self):
        """Initialize an empty library."""
        self._books = []  # Private list of Book objects

    def add_book(self, book):
        """Add a new book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Book titled '{title}' not found in library.")

    def return_book(self, title):
        """Return a book by title if found."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"Book titled '{title}' not found in library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
