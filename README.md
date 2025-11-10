library-management-oop/
│
├── README.md
│
├── procedural_version/
│ ├── library_procedural.py
│ └── test_procedural.py
│
└── oop_solution/
├── library_oop.py
└── test_oop.py

Design Overview

**Book**
- Attributes: `id`, `title`, `author`, `total_copies`, `available_copies`
- Methods: `borrow()`, `return_book()`

**Member**
- Attributes: `id`, `name`, `email`, `borrowed_books`
- Methods: `borrow_book(book)`, `return_book(book)`

**Library**
- Attributes: `books`, `members`, `borrowed_books`
- Methods: `add_book()`, `add_member()`, `borrow_book()`, `return_book()`, `display_available_books()`, `display_member_books()`

Testing
`test_oop.py` verifies:
- Adding books and members  
- Borrowing and returning books  
- Displaying available books and member records  
- Handling edge cases:
  - Borrowing unavailable books  
  - Borrowing limit exceeded  
  - Returning unborrowed or nonexistent books/members  

Run Tests
bash
oop_solution
python test_oop.py
