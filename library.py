books = []

def show_menu():
    print(">-----<     LIBRARY MANAGEMENT SYSTEM     >-----<")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Exit")
    

def add_book():
    
    name = input("Enter book name : ")
    author = input("Enter author name : ")

    book = {
        "name": name,
        "author": author,
        "borrowed": False
    }

    books.append(book)
    print("✅ Book added successfully!")
    

def view_books():
    print("\nBooks in Library : ")
            
    for book in books:
        status = "Borrowed" if book["borrowed"] else "Available"
        
        print("Book Name :", book["name"])
        print("Author    :", book["author"])
        print("Status    :", status)
        print("-------------------------")
    

def find_book(search):
    for book in books:
        if search == book["name"].lower():
            return book
    return None

def search_book():
    search = input("Enter book name to search : ").lower()
    
    book = find_book(search)
    
    if book:
        print("✅ Book found!")
        print("Book Name :", book["name"])
        print("Author    :", book["author"])
        print("Status    :", "Borrowed" if book["borrowed"] else "Available")
    else:
        print("❌ Book not found!")


def delete_book():
    search = input("Enter book name to delete : ").lower()
    
    book = find_book(search)
    
    if book:
        books.remove(book)
        print("✅ Book deleted successfully!")
        print("Book Name :", book["name"])
        print("Author    :", book["author"])
        print("Status    :", "Borrowed" if book["borrowed"] else "Available")
    else:
        print("❌ Book not found!")


def borrow_book():
    search = input("Enter book name to borrow : ").lower()
    
    book = find_book(search)
    
    if book:
        if not book["borrowed"]:
            book["borrowed"] = True
            print("✅ Book borrowed successfully!")
            print("Book Name :", book["name"])
            print("Author    :", book["author"])
            print("Status    :", "Borrowed" if book["borrowed"] else "Available")
        else:
            print("❌ Book is already borrowed!")
    else:
        print("❌ Book not found!")


def return_book():
    search = input("Enter book name to return : ").lower()
    
    book = find_book(search)

    if book:
        if book["borrowed"]:
            book["borrowed"] = False
            print("✅ Book returned successfully!")
            print("Book Name :", book["name"])
            print("Author    :", book["author"])
            print("Status    :", "Borrowed" if book["borrowed"] else "Available")
        else:
            print("❌ Book was not borrowed!")
    else:
        print("❌ Book not found!")
        

while True:
    show_menu()
    
    choice = input("Enter your choice : ")
    
    if choice == '1':
        add_book()
        
    elif choice == '2':
        view_books()
        
    elif choice == '3':
        search_book()
        
    elif choice == '4':
        delete_book()
        
    elif choice == '5':
        borrow_book()
        
    elif choice == '6':
        return_book()
        
    elif choice == '7':
        print("Thank you for using the Library Management System.")
        break
    
    else:
        print("Invalid choice! Please try again.")
        
