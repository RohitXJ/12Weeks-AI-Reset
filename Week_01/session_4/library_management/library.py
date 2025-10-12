from abstr_lib import LibraryEntity
from member import Member
from book import Book

class Library(LibraryEntity):
    __books = []
    __members = []

    def add_book(self, book):
        self.__books.append(book)
    
    def add_member(self, member):
        self.__members.append(member)
    
    def issue_book(self, book_title, member_id):
        member_found = None
        for member in self.__members:
            if member.get_member_id() == member_id:
                member_found = member
                break
        
        if not member_found:
            print(f"Member with ID {member_id} not found.")
            return

        book_found = None
        for book in self.__books:
            if book.get_title() == book_title:
                book_found = book
                break

        if not book_found:
            print(f"Book with title '{book_title}' not found.")
            return

        if book_found.is_available():
            book_found.mark_issued()
            member_found.borrow_book(book_found)
            print(f"Book '{book_title}' issued to member {member_found.get_name()}.")
        else:
            print(f"Sorry, the book '{book_title}' is currently unavailable.")
    
    def return_book_to_library(self, book_title, member_id):
        member_found = None
        for member in self.__members:
            if member.get_member_id() == member_id:
                member_found = member
                break
        
        if not member_found:
            print(f"Member with ID {member_id} not found.")
            return

        book_found = None
        for book in self.__books:
            if book.get_title() == book_title:
                book_found = book
                break

        if not book_found:
            print(f"Book with title '{book_title}' not found.")
            return

        if not book_found.is_available():
            book_found.mark_returned()
            member_found.return_book(book_found)
            print(f"Book '{book_title}' returned by member {member_found.get_name()}.")
        else:
            print(f"Sorry, the book '{book_title}' was not issued.")
    
    def show_inventory(self):
        for book in self.__books:
            print(f"{book.get_details()}\nisbn : {book.get_isbn()}\n Available Status :{"Available" if book.is_available() else "Not Available"}\n")
    
    def find_book(self, title):
        for book in self.__books:
            if book.get_title() == title:
                return True
        return False

