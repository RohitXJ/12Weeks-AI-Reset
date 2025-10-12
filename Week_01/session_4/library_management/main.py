from library import Library
from book import Book
from member import Member

def main():
    library = Library()
    # Adding some initial data for demonstration
    book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "978-0345391803")
    book2 = Book("The Lord of the Rings", "J.R.R. Tolkien", "978-0618640157")
    member1 = Member("Alice", "M001")
    member2 = Member("Bob", "M002")
    library.add_book(book1)
    library.add_book(book2)
    library.add_member(member1)
    library.add_member(member2)

    while True:
        print("\n--- Library Management System ---")
        print("1. Add a new book")
        print("2. Add a new member")
        print("3. Issue a book")
        print("4. Return a book")
        print("5. Show inventory")
        print("6. Find a book")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            new_book = Book(title, author, isbn)
            library.add_book(new_book)
            print(f"Book '{title}' added successfully.")

        elif choice == '2':
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            new_member = Member(name, member_id)
            library.add_member(new_member)
            print(f"Member '{name}' added successfully.")

        elif choice == '3':
            book_title = input("Enter the title of the book to issue: ")
            member_id = input("Enter the member ID: ")
            library.issue_book(book_title, member_id)

        elif choice == '4':
            book_title = input("Enter the title of the book to return: ")
            member_id = input("Enter the member ID: ")
            library.return_book_to_library(book_title, member_id)

        elif choice == '5':
            print("\n--- Library Inventory ---")
            library.show_inventory()

        elif choice == '6':
            title = input("Enter the title of the book to find: ")
            if library.find_book(title):
                print(f"Book '{title}' is in the library.")
            else:
                print(f"Book '{title}' not found.")

        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
