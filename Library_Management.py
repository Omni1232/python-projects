class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        book_id = input("Enter book ID: ")
        book = Book(title, author)
        self.books[book_id] = book
        print(f"Book '{title}' by {author} added successfully with ID {book_id}.")

    def register_member(self):
        name = input("Enter member name: ")
        member_id = input("Enter member ID: ")
        member = Member(name, member_id)
        self.members[member_id] = member
        print(f"Member '{name}' registered successfully with ID {member_id}.")

    def issue_book(self):
        member_id = input("Enter member ID: ")
        book_id = input("Enter book ID: ")

        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]

            if book.is_available:
                member.borrowed_books.append(book)
                book.is_available = False
                print(f"Book '{book.title}' issued to member '{member.name}'.")
            else:
                print(f"Book '{book.title}' is currently not available.")
        else:
            print("Invalid member ID or book ID.")

    def return_book(self):
        member_id = input("Enter member ID: ")
        book_id = input("Enter book ID: ")

        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]

            if book in member.borrowed_books:
                member.borrowed_books.remove(book)
                book.is_available = True
                print(f"Book '{book.title}' returned by member '{member.name}'.")
            else:
                print(f"Member '{member.name}' did not borrow book '{book.title}'.")
        else:
            print("Invalid member ID or book ID.")

    def display_books(self):
        print("Available books in the library:")
        for book_id, book in self.books.items():
            status = "Available" if book.is_available == True else "Issued"
            print(f"ID: {book_id}, Title: '{book.title}', Author: {book.author}, Status: {status}")


    def display_members(self):
        print("Registered members in the library:")
        for member_id, member in self.members.items():
            print(f"ID: {member_id}, Name: '{member.name}'")

library = Library()

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Members")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        library.add_book()
    elif choice == '2':
        library.register_member()
    elif choice == '3':
        library.issue_book()
    elif choice == '4':
        library.return_book()
    elif choice == '5':
        library.display_books()
    elif choice == '6':
        library.display_members()
    elif choice == '7':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
