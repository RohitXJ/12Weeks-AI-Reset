from abstr_lib import LibraryEntity

class Member(LibraryEntity):
    def __init__(self,name,member_id):
        self.__name = name
        self.__member_id = member_id
        self.__borrowed_books = []


    def get_member_id(self):
        return self.__member_id

    def get_name(self):
        return self.__name

    def borrow_book(self, book):
        self.__borrowed_books.append(book)
    
    def return_book(self, book):
        self.__borrowed_books.remove(book)
    
    def get_borrowed_books(self):
        return self.__borrowed_books