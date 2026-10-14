'''
Write a python program that allows a librarian to add several books to a library. 
For each book, ask the user ot enter it's title and the number of copies. Store each book and it's 
available copy count in a dictionary. 

Apply the books have been added, display a menu that lets the user issue a book, return a book, 
display all books, or exit the program. 

Apply these conditions:
- Book titles should be compared without distinguishing uppercase and lowercase letters.
- A book can be issues only if it exists in the library and at least one copy is avialable.
- Issuing a book decreased it's available copy count by one. 
- A book can be returned only if it exists in the library and at least one copy has copy has 
already been issued. 
- Returning a book increases it's available copy count by one. 
- Display an appropriate message for an unavailable book, an invalid choice, or an invalid number
of copies. 
'''

class Library:
    def __init__(self):
        self.books = {}
        self.issued = {}
    def add_books(self):
        n = int(input("Enter number of books: "))
        for i in range(n):
            title = input("Enter book title: ").lower()
            copies = int(input("Enter number of copies: "))
            if copies < 0:
                print("Invalid number of copies!")
            else:
                self.books[title] = copies
                self.issued[title] = 0
    def issue_book(self):
        title = input("Enter book title: ").lower()
        if title not in self.books:
            print("Book not available!")
        elif self.books[title] > 0:
            self.books[title] -= 1
            self.issued[title] += 1
            print("Book issued successfully!")
        else:
            print("No copies available!")
    def return_book(self):
        title = input("Enter book title: ").lower()
        if title not in self.books:
            print("Book not available!")
        elif self.issued[title] > 0:
            self.books[title] += 1
            self.issued[title] -= 1
            print("Book returned successfully!")
        else:
            print("No book has been issued!")
    def display_books(self):
        for title in self.books:
            print(title, ":", self.books[title], "copies available")
library = Library()
library.add_books()
while True:
    print("\n1. Issue Book")
    print("2. Return Book")
    print("3. Display Books")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        library.issue_book()
    elif choice == "2":
        library.return_book()
    elif choice == "3":
        library.display_books()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

