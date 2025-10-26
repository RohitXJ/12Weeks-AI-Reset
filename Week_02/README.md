# Week 2: Data Structures in Python

![Data Structures](https://media.geeksforgeeks.org/wp-content/uploads/20211021164218/pythondatastructuresmin.png)

Welcome to the summary of Week 2 of the 12-Week AI Reset program. This week was a deep dive into fundamental data structures, moving from Python's built-in types to more complex, custom-built structures like Linked Lists, Stacks, Queues, and Trees.

All exercises and implementations were completed in Jupyter Notebooks.

---

## 📝 Table of Contents

1.  [Session 1: Built-in Data Structures Review](#session-1-built-in-data-structures-review)
2.  [Session 2: Core Data Structures](#session-2-core-data-structures)
    - [Linked Lists](#linked-lists)
    - [Stacks](#stacks)
    - [Queues](#queues)
3.  [Session 3: Trees (Binary Search Trees)](#session-3-trees-binary-search-trees)

---

## Session 1: Built-in Data Structures Review

This session, covered in `session_1.ipynb`, served as a refresher and problem-solving session on Python's essential built-in data structures.

### Lists, Tuples, Sets, and Dictionaries
- **List**: Implemented algorithms for finding the second largest number, removing duplicates, reversing in-place, finding common elements, and moving all zeros to the end.
- **Tuple**: Practiced counting element occurrences, flattening a tuple of tuples, and finding min/max elements without using built-in functions.
- **Set**: Solved problems on finding unique elements, checking for subsets, finding symmetric differences, and removing elements based on a condition.
- **Dictionary**: Worked on character frequency counting, merging dictionaries with value addition, finding the key with the maximum value, inverting a dictionary, and sorting by value.

---

## Session 2: Core Data Structures

This session was dedicated to implementing and understanding the mechanics of foundational data structures from scratch.

### Linked Lists
In `session_2_LinkedList.ipynb`, a Singly Linked List was built from the ground up.
- **Implementation**: Created `Node` and `SinglyLinkedList` classes.
- **Core Operations**: Implemented methods for insertion (at head and tail), deletion (by value), and traversal.
- **Advanced Operations**:
  - **Reversal**: An in-place algorithm to reverse the list by manipulating `next` pointers.
  - **Middle Node**: Found the middle of the list in a single pass using the fast and slow pointer technique.

### Stacks
The `session_2_Stack.ipynb` notebook focused on the Last-In, First-Out (LIFO) principle of stacks.
- **Implementation**: A `Stack` class was created manually using a Python list.
- **Applications**:
  - Reversing a string.
  - Checking for balanced parentheses in an expression.
  - Converting decimal numbers to their binary representation.
- **Advanced Problems**:
  - **Min in O(1)**: Designed a stack that could return the minimum element in constant time.
  - **Infix to Postfix**: Implemented an algorithm to convert infix mathematical expressions to postfix notation.

### Queues
The `session_2_Queue.ipynb` notebook explored the First-In, First-Out (FIFO) principle.
- **Implementation**:
  - A basic `Queue` using `collections.deque`.
  - A fixed-size `CircularQueue` to handle wraparound logic.
  - A `Queue` implemented using two stacks to simulate FIFO behavior.
- **Conceptual Topics**:
  - **Priority Queue**: Discussed the concept where elements are served based on priority, not just arrival time.
  - **Level Order Traversal**: Explained how a queue is fundamental to performing a Breadth-First Search (BFS) on a tree or graph.

---

## Session 3: Trees (Binary Search Trees)

The final session of the week, in `session_3_Tree.ipynb`, introduced a non-linear data structure: the Binary Search Tree (BST).

### BST Implementation and Traversal
- **Core Components**: Created a `TreeNode` class and implemented a recursive `insert` function to build the BST.
- **Traversals**:
  - **Inorder Traversal**: Implemented a function that visits nodes in `Left -> Root -> Right` order, which results in a sorted sequence of the node values.
  - **Level Order Traversal**: Used a queue to visit the tree level by level (BFS).

### BST Operations and Validation
- **Core Functions**: Implemented recursive functions for `search`, `find_min`, and calculating the `max_depth` (height) of the tree.
- **Validation**: Created a function `is_valid_bst` to verify if a given binary tree adheres to the properties of a Binary Search Tree by passing min/max constraints through the recursion.
