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
    
def search_book():
    search = input("Enter book name to search : ").lower()
    
    found = False
    
    for book in books:
        if search == book["name"].lower():
            found = True
            break
    if found:
        print("✅ Book found!")
    else:
        print("❌ Book not found!")
        
def delete_book():
    search = input("Enter book name to delete: ").lower()

    found = False

    for book in books:
        if search == book["name"].lower():
            books.remove(book)
            found = True
            break

    if found:
        print("✅ Book deleted successfully!")
    else:
        print("❌ Book not found!")
        
def borrow_book():
    search = input("Enter book name to borrow : ").lower()
    
    found = False
    
    for book in books:
        if search == book["name"].lower():
            found = True
            if not book["borrowed"]:
                book["borrowed"] = True
                print("✅ Book borrowed successfully!")
                break
            
            else:
                print("❌ Book is already borrowed!")
                break
            
    if not found:
                print("❌ Book not found!")

def return_book():
    search = input("Enter book name to return : ").lower()
    
    found = False
    
    for book in books:
        if search == book["name"].lower():
            found = True
            if book["borrowed"]:
                book["borrowed"] = False
                print("✅ Book returned successfully!")
                break
            else:
                print("❌ Book was not borrowed!")
                break
            
    if not found:
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
        
