# Library Management System

This project is a simple command-line-based Library Management System implemented in Python. It allows users to manage books and members, issue books to members, and handle returns.

## Core Components

The system is built around a few key classes:

### `Book`
- Represents a book in the library.
- **Attributes**:
    - `title`: The title of the book.
    - `author`: The author of the book.
    - `isbn`: The ISBN of the book.
    - `available`: A boolean indicating if the book is currently available.
- **Methods**:
    - `get_details()`: Returns the book's title and author.
    - `is_available()`: Checks if the book is available.
    - `mark_issued()`: Marks the book as unavailable.
    - `mark_returned()`: Marks the book as available.

### `Member`
- Represents a library member.
- **Attributes**:
    - `name`: The name of the member.
    - `member_id`: A unique ID for the member.
    - `borrowed_books`: A list of `Book` objects the member has borrowed.
- **Methods**:
    - `borrow_book(book)`: Adds a book to the member's borrowed list.
    - `return_book(book)`: Removes a book from the member's borrowed list.

### `Library`
- The central class that manages the entire system.
- Manages a collection of `Book` and `Member` objects.
- **Methods**:
    - `add_book(book)`: Adds a new book to the library's inventory.
    - `add_member(member)`: Registers a new member.
    - `issue_book(book_title, member_id)`: Handles the process of a member borrowing a book.
    - `return_book_to_library(book_title, member_id)`: Handles the process of a member returning a book.
    - `show_inventory()`: Displays all books in the library and their availability status.
    - `find_book(title)`: Searches for a book by its title.

### `LibraryEntity` (Abstract Base Class)
- An abstract class that defines a common interface for the `Book`, `Member`, and `Library` classes. This is intended to enforce a standard structure but is not fully implemented as a true abstract base class in this version.

## How It Works

The `main.py` script provides a simple command-line interface (CLI) that allows a user to interact with the library. The user can choose from a menu of options to:
1.  Add a new book to the inventory.
2.  Add a new library member.
3.  Issue a book to a member.
4.  Return a book.
5.  View the entire library inventory.
6.  Find a specific book by title.

The program runs in a loop, continuously prompting the user for input until they choose to exit.
