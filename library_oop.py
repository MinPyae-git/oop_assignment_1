class Book:
    """Represents a single book in the library."""
    
    def __init__(self, book_id, title, author, total_copies):
        self.id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow(self):
        """Borrow a book if copies are available."""
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    def return_book(self):
        """Return a borrowed book."""
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False

    def __str__(self):
        return f"{self.title} by {self.author} ({self.available_copies}/{self.total_copies} available)"


class Member:
    """Represents a library member."""
    
    def __init__(self, member_id, name, email):
        self.id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        """Borrow a book if limit not reached and copies available."""
        if len(self.borrowed_books) >= 3:
            print(f"Error: {self.name} has reached borrowing limit!")
            return False
        if not book.borrow():
            print(f"Error: No copies available for '{book.title}'!")
            return False

        self.borrowed_books.append(book.id)
        print(f"{self.name} borrowed '{book.title}'")
        return True

    def return_book(self, book: Book):
        """Return a borrowed book."""
        if book.id not in self.borrowed_books:
            print(f"Error: {self.name} hasn't borrowed '{book.title}'!")
            return False
        book.return_book()
        self.borrowed_books.remove(book.id)
        print(f"{self.name} returned '{book.title}'")
        return True

    def __str__(self):
        return f"{self.name} ({len(self.borrowed_books)} books borrowed)"


class Library:
    """Central system to manage books and members."""
    
    def __init__(self):
        self.books = []
        self.members = []
        self.borrowed_books = []  


    def add_book(self, book_id, title, author, total_copies):
        book = Book(book_id, title, author, total_copies)
        self.books.append(book)
        print(f"Book '{title}' added successfully!")

    def add_member(self, member_id, name, email):
        member = Member(member_id, name, email)
        self.members.append(member)
        print(f"Member '{name}' registered successfully!")

    def find_book(self, book_id):
        for b in self.books:
            if b.id == book_id:
                return b
        return None

    def find_member(self, member_id):
        for m in self.members:
            if m.id == member_id:
                return m
        return None



    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member:
            print("Error: Member not found!")
            return
        if not book:
            print("Error: Book not found!")
            return

        if member.borrow_book(book):
            self.borrowed_books.append({
                'member_id': member.id,
                'book_id': book.id,
                'member_name': member.name,
                'book_title': book.title
            })

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member or not book:
            print("Error: Member or Book not found!")
            return

        if member.return_book(book):
            self.borrowed_books = [
                t for t in self.borrowed_books
                if not (t['member_id'] == member_id and t['book_id'] == book_id)
            ]


    def display_available_books(self):
        print("\n=== Available Books ===")
        for b in self.books:
            if b.available_copies > 0:
                print(b)
        if all(b.available_copies == 0 for b in self.books):
            print("No books currently available.")

    def display_member_books(self, member_id):
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return

        print(f"\n=== Books borrowed by {member.name} ===")
        if not member.borrowed_books:
            print("No books currently borrowed.")
        else:
            for bid in member.borrowed_books:
                book = self.find_book(bid)
                if book:
                    print(f"- {book.title} by {book.author}")



if __name__ == "__main__":
    lib = Library()
    lib.add_book(1, "Python Crash Course", "Eric Matthes", 3)
    lib.add_member(101, "Alice", "alice@email.com")
    lib.borrow_book(101, 1)
    lib.display_member_books(101)
    lib.return_book(101, 1)
    lib.display_available_books()
