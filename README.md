# 📚 Library Management System

A simple and beginner-friendly **Library Management System** built using **Python**. This is a console-based application that allows users to manage books through an interactive menu-driven interface.

The project demonstrates fundamental Python programming concepts such as **functions, lists, dictionaries, loops, conditional statements, user input handling, string manipulation, and basic data management**. Each book is stored as a dictionary containing its **name**, **author**, and **borrowing status**.


# 🚀 Features

* ➕ Add new books with their author names
* 📖 View all books in the library
* 🔍 Search for books by name
* ❌ Delete books from the library
* 📚 Borrow available books
* 🔄 Return borrowed books
* 🔠 Case-insensitive search, deletion, borrowing, and returning
* 📋 Display complete book details:

  * Book Name
  * Author Name
  * Current Status (`Available` or `Borrowed`)
* ✅ User-friendly success and error messages
* 🖥️ Interactive menu-driven command-line interface
* 🐍 Built entirely with Python


# 🛠️ Technologies Used

* Python 3


# 📂 Project Structure

```text
library-management-system/
│
├── library.py
└── README.md
```

---

# ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/library-management-system.git
```

### 2. Navigate to the project directory

```bash
cd library-management-system
```

### 3. Run the application

```bash
python library.py
```


# 💻 Sample Menu

```text
>-----<     LIBRARY MANAGEMENT SYSTEM     >-----<

1. Add Book
2. View Books
3. Search Book
4. Delete Book
5. Borrow Book
6. Return Book
7. Exit
```

---

# 📝 Sample Execution

```text
Enter your choice : 1

Enter book name : Python Crash Course
Enter author name : Eric Matthes

✅ Book added successfully!

Enter your choice : 2

Books in Library :

Book Name : Python Crash Course
Author    : Eric Matthes
Status    : Available
-------------------------

Enter your choice : 5

Enter book name to borrow : python crash course

✅ Book borrowed successfully!

Enter your choice : 2

Books in Library :

Book Name : Python Crash Course
Author    : Eric Matthes
Status    : Borrowed
-------------------------

Enter your choice : 6

Enter book name to return : Python Crash Course

✅ Book returned successfully!
```


# 📚 Python Concepts Practiced

* Variables
* Lists
* Dictionaries
* Functions
* `while` Loops
* `for` Loops
* Conditional Statements (`if`, `elif`, `else`)
* Boolean Values (`True` / `False`)
* User Input (`input()`)
* String Methods (`lower()`)
* List Operations (`append()` and `remove()`)
* Dictionary Access and Modification
* Linear Search
* Menu-Driven Programming


# 🔮 Future Improvements

This project will continue to be upgraded with additional features, including:

* ✏️ Update existing book details
* 💾 Save library data to a file (`books.txt`)
* 📂 Automatically load saved data at startup
* 🆔 Assign unique IDs to books
* 📅 Track borrow and return dates
* 👥 Support multiple users
* 📊 Display the total number of books
* 🔢 Sort books alphabetically
* 🗄️ Integrate an SQLite database
* 🏗️ Refactor the project using Object-Oriented Programming (OOP)
* 🔒 Add user authentication and admin features
* ✅ Improve input validation and exception handling


# 🎯 Purpose

This project was created as part of my Python learning journey to strengthen programming fundamentals by building a real-world console application. It serves as a foundation for implementing more advanced features such as persistent storage, databases, and object-oriented programming.


# 🤝 Contributions

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository, open an issue, or submit a pull request.


# 📄 License

This project is open source and intended for learning and educational purposes.
