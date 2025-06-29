# library_management.py

class Book:
    """
    Represents a book in the library with a title, author, and availability status.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False # Already checked out

    def return_book(self):
        """Marks the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False # Not checked out

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out

    def __str__(self):
        """String representation for the Book object."""
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book objects, allowing adding, checking out,
    returning, and listing available books.
    """
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Adds a Book object to the library's collection."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print(f"Error: Cannot add {type(book).__name__}. Only Book objects can be added.")

    def check_out_book(self, title):
        """
        Checks out a book by its title. If found and available, marks it as checked out.
        """
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                    return True
                else:
                    print(f"'{title}' is already checked out.")
                    return False
        print(f"'{title}' not found in the library.")
        return False

    def return_book(self, title):
        """
        Returns a book by its title. If found and checked out, marks it as available.
        """
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                    return True
                else:
                    print(f"'{title}' was not checked out.")
                    return False
        print(f"'{title}' not found in the library.")
        return False

    def list_available_books(self):
        """Lists all books that are currently available in the library."""
        available_found = False
        for book in self._books:
            if book.is_available():
                print(book)
                available_found = True
        if not available_found:
            print("No books are currently available.")