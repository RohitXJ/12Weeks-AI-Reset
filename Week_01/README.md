
# Week 1: Python Fundamentals & Object-Oriented Programming

![Python Logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

Welcome to the summary of Week 1 of the 12-Week AI Reset program. This week was dedicated to building a strong foundation in Python, starting from the very basics and culminating in a complete Object-Oriented Programming (OOP) project.

All exercises and projects were completed using Jupyter Notebooks.

---

## 📝 Table of Contents

1.  [Session 1: Python Basics](#session-1-python-basics)
2.  [Session 2: Advanced Data Structures & Functional Tools](#session-2-advanced-data-structures--functional-tools)
3.  [Session 3: Modules, Error Handling, and File I/O](#session-3-modules-error-handling-and-file-io)
4.  [Session 4: Object-Oriented Programming (OOP)](#session-4-object-oriented-programming-oop)
5.  [Project: Library Management System](#project-library-management-system)

---

## Session 1: Python Basics

This session covered the fundamental building blocks of Python programming. The notebook `session_1.ipynb` contains hands-on exercises on:

### Variables & Data Types
- Swapping two numbers without a temporary variable.
- Reversing a string using a loop.
- Type casting user input into integer and float.
- Basic arithmetic operations and string manipulations.

### Conditionals & Loops
- **FizzBuzz Challenge**: A classic programming task to print numbers from 1 to 50 with special conditions for multiples of 3, 5, and both.
- Vowel Counting: Iterating through a string to count the number of vowels.
- Factorial Calculation: Implemented using both `for` and `while` loops.
- Prime Number Checker: A function to determine if a number is prime.

### Functions
- Creating simple functions for greeting and finding the maximum element in a list.
- A function to analyze a string and count uppercase letters, lowercase letters, digits, and special characters.
- Palindrome checker.

---

## Session 2: Advanced Data Structures & Functional Tools

This session, detailed in `session_2.ipynb`, explored more efficient and Pythonic ways to handle data.

### Smart Logic & List/Dictionaries
- **List Comprehensions**: Creating lists in a single, readable line (e.g., squaring numbers, filtering even/odd numbers).
- **Dictionary Comprehensions**: Building dictionaries dynamically (e.g., mapping fruits to their string lengths).

### Lambda, Map, Filter, Reduce
- **`lambda` functions**: Creating small, anonymous functions for quick operations.
- **`map()`**: Applying a function to every item in an iterable (e.g., converting Celsius to Fahrenheit).
- **`filter()`**: Filtering elements from an iterable based on a condition (e.g., keeping names with length greater than 5).
- **`reduce()`**: Cumulatively applying a function to items in a sequence to reduce it to a single value (e.g., calculating the product of a list).

---

## Session 3: Modules, Error Handling, and File I/O

`session_3.ipynb` focused on making code more robust, modular, and interactive with the file system.

### Exception Handling
- Using `try...except` blocks to handle errors gracefully (e.g., `ZeroDivisionError`, `ValueError`, `FileNotFoundError`).
- Utilizing `else` and `finally` clauses to execute code when no errors occur or after the `try...except` block has finished.
- Raising custom exceptions.

### Modules & Packages
- Creating custom modules for mathematical operations (`math_func.py`) and greetings (`greet_func.py`).
- Building a simple Python package (`myPackages`) and importing modules from it.
- Understanding the difference between `import module` and `from module import function`.

### File I/O
- **JSON**: Serializing Python dictionaries to JSON strings and files, and deserializing them back.
- **CSV**: Writing data to and reading data from CSV files using the `csv` module.
- **Pickle**: Serializing Python objects to a binary format and deserializing them back, preserving their structure.

### Logging
- Setting up basic logging to record informational messages and errors to a file (`app.log`).
- Logging simulated user login attempts and exceptions.

---

## Session 4: Object-Oriented Programming (OOP)

`session_4.ipynb` was an introduction to the OOP paradigm in Python, a crucial concept for building scalable and maintainable applications.

### Core OOP Concepts Covered
- **Classes and Objects**: Creating blueprints (`class`) and instances (`object`).
- **`__init__()`**: The constructor method for initializing object attributes.
- **Instance vs. Class Variables**: Differentiating between variables tied to an object and those shared by all instances of a class.
- **Methods**: Defining functions within a class that operate on object data.
  - **`@classmethod`**: Methods that operate on the class itself, not the instance.
  - **`@staticmethod`**: Utility functions that are related to the class but do not depend on class or instance state.
- **Encapsulation**: Protecting data by making attributes private (e.g., `__balance`) and providing public getter and setter methods.
- **Inheritance**: Creating a child class (`Employee`) that inherits attributes and methods from a parent class (`Person`).
- **Polymorphism**: Allowing objects of different classes to respond to the same method call (`make_sound()`) in their own unique ways.
- **Abstraction**: Using abstract base classes (`ABC`) to define a common interface for a set of subclasses.

---

## Project: Library Management System

As a culmination of the week's learning, a command-line Library Management System was developed. This project integrates all the OOP concepts learned in Session 4.

### Project Structure
The project is organized into several Python files:
- `main.py`: The entry point of the application, containing the user interface logic.
- `book.py`: Contains the `Book` class.
- `member.py`: Contains the `Member` class.
- `library.py`: Contains the `Library` class, which manages the books and members.
- `abstr_lib.py`: An abstract base class to define a common structure.

### Features
- **Add and Manage Books**: Add new books to the library inventory.
- **Register Members**: Add new members to the system.
- **Issue and Return Books**: Manage the process of borrowing and returning books, updating their availability status.
- **View Inventory**: Display a list of all books and their current status.
- **Encapsulation**: Attributes of the classes are kept private, and access is controlled through methods.
