class Book:
    """
    Base class for a book with common attributes: title and author.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the Book object.
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Derived class for an EBook, inheriting from Book and adding file_size.
    """
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size

    def __str__(self):
        """
        Returns a string representation of the EBook object,
        including file size.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Derived class for a PrintBook, inheriting from Book and adding page_count.
    """
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count

    def __str__(self):
        """
        Returns a string representation of the PrintBook object,
        including page count.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Manages a collection of various book types (Book, EBook, PrintBook)
    demonstrating composition.
    """
    def __init__(self):
        self.books = []  # List to store book instances

    def add_book(self, book):
        """
        Adds a Book (or derived type) instance to the library's collection.
        """
        if isinstance(book, Book):  # Ensure only book objects are added
            self.books.append(book)
        else:
            print(f"Cannot add {type(book).__name__}. Only Book objects can be added to the library.")

    def list_books(self):
        """
        Prints details of each book in the library.
        Uses the __str__ method of each book object.
        """
        if not self.books:
            print("The library is empty.")
            return

        for book in self.books:
            print(book) 