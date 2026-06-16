books = []

def show_menu():
    print(">-----<     LIBRARY MANAGEMENT SYSTEM     >-----<")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")
    
def add_book():
    book = input("Enter book name : ")
    books.append(book)
    print("✅ Book added successfully!")
    
def view_books():
    print("\nBooks in Library : ")
        
    for book in books:
        print(book)
    
def search_book():
    search = input("Enter book name to search : ").lower()
    
    found = False
    
    for book in books:
        if search == book.lower():
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
        if search == book.lower():
            books.remove(book)
            found = True
            break

    if found:
        print("✅ Book deleted successfully!")
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
        print("Thank you for using the Library Management System.")
        break
    
    else:
        print("Invalid choice! Please try again.")
        
