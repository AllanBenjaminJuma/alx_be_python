# book_class.py

class Book:
    """
    A class to represent a book, demonstrating Python's magic methods.
    """
    def __init__(self, title, author, year):
        """
        Initializes a Book instance with a title, author, and publication year.
        """
        self.title = title
        self.author = author
        self.year = year
        # Removed: print(f"Book '{self.title}' created.")

    def __del__(self):
        """
        Destructor method, called when the Book object is about to be destroyed.
        Prints a message indicating the book being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book object.
        Used by print() and str() functions.
        Format: "(title) by (author), published in (year)"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an official string representation of the Book object.
        This string should be unambiguous and, if possible, allow recreation of the object.
        Used by repr() and in interactive console.
        Format: f"Book('{self.title}', '{self.author}', {self.year})"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"