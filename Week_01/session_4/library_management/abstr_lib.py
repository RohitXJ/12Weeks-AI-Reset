class LibraryEntity:
    """
    Abstract base class defining all core attributes and method signatures
    for Book, Member, and Library classes in the system.
    """

    # ----- Common -----
    def __init__(self):
        self._id = None
        self._name = None

    # ----- Book Methods -----
    def get_details(self):
        pass

    def is_available(self):
        pass

    def mark_issued(self):
        pass

    def mark_returned(self):
        pass

    # ----- Member Methods -----
    def borrow_book(self, book):
        pass

    def return_book(self, book):
        pass

    def get_borrowed_books(self):
        pass

    # ----- Library Methods -----
    def add_book(self, book):
        pass

    def add_member(self, member):
        pass

    def issue_book(self, book_title, member_id):
        pass

    def return_book_to_library(self, book_title, member_id):
        pass

    def show_inventory(self):
        pass

    def find_book(self, title):
        pass
