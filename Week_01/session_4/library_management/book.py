from abstr_lib import LibraryEntity

class Book(LibraryEntity):
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__available = True


    def get_title(self):
        return self.__title
    
    def get_details(self):
        return f"{self.__title} By {self.__author}"
    
    def get_isbn(self):
        return self.__isbn
    
    def is_available(self):
        return self.__available
    
    def mark_issued(self):
        self.__available = False
    
    def mark_returned(self):
        self.__available = True