from library_oop import Library

def test_library_system():
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM (OOP VERSION) - COMPREHENSIVE TEST")
    print("=" * 60)

    lib = Library()

    
    print("\n--- TEST 1: Adding Books ---")
    lib.add_book(1, "Python Crash Course", "Eric Matthes", 3)
    lib.add_book(2, "Clean Code", "Robert Martin", 2)
    lib.add_book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)
    lib.add_book(4, "Design Patterns", "Gang of Four", 2)

    
    print("\n--- TEST 2: Registering Members ---")
    lib.add_member(101, "Alice Smith", "alice@email.com")
    lib.add_member(102, "Bob Jones", "bob@email.com")
    lib.add_member(103, "Carol White", "carol@email.com")

    
    print("\n--- TEST 3: Display Available Books ---")
    lib.display_available_books()


    print("\n--- TEST 4: Successful Borrowing ---")
    lib.borrow_book(101, 1)
    lib.borrow_book(101, 2)
    lib.borrow_book(102, 1)


    print("\n--- TEST 5: Display Member's Books ---")
    lib.display_member_books(101)
    lib.display_member_books(102)
    lib.display_member_books(103)

    print("\n--- TEST 6: Borrowing Last Copy ---")
    lib.borrow_book(103, 3)
    lib.display_available_books()

  
    print("\n--- TEST 7: Attempting to Borrow Unavailable Book ---")
    lib.borrow_book(102, 3)

    
    print("\n--- TEST 8: Borrowing Limit Test ---")
    lib.borrow_book(101, 4)
    lib.display_member_books(101)
    lib.borrow_book(101, 3)

    
    print("\n--- TEST 9: Returning Books ---")
    lib.return_book(101, 1)
    lib.return_book(102, 1)
    lib.display_available_books()

    
    print("\n--- TEST 10: Attempting Invalid Return ---")
    lib.return_book(102, 2)

   
    print("\n--- TEST 11: Return and Re-borrow ---")
    lib.return_book(103, 3)
    lib.borrow_book(102, 3)
    lib.display_member_books(102)

    
    print("\n--- TEST 12: Error Handling ---")
    lib.borrow_book(999, 1)
    lib.borrow_book(101, 999)
    lib.return_book(999, 1)
    lib.display_member_books(999)

    print("\n--- FINAL LIBRARY STATUS ---")
    lib.display_available_books()

    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    test_library_system()
