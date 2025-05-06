# 📚 Davina's Library System (Python CLI App)

This is a simple, text-based **Library Management System** written in Python. Users can borrow and return books using the command line. This project is ideal for beginners who want to learn about Python data types and control flow.

---

## ✨ Features

- 📖 View all books grouped by genre
- 👤 View a list of registered users
- 🔐 Log in using your name
- ✅ See what books you've borrowed
- 📚 Borrow a book (if not already borrowed)
- 📤 Return a borrowed book

---

## 🧱 How It Works

### 1. 📘 Book Data

Books are stored using a **dictionary**. Each book has a unique ID (like `B001`) and contains:

- Title
- Author
- Genre

Example:

```python
books = {
    "B001": ("The Alchemist", "Paulo Coelho", "Fiction")
}
```

---

### 2. 🎨 Genres

Genres are stored in a **set**:

```python
genres = {
    "Fiction", "Dystopian", "Classic", ...
}
```

This ensures no duplicates and makes it easy to organize books.

---

### 3. 🗂️ Books by Genre

Books are grouped into genres using a dictionary called `books_by_genre`:

```python
books_by_genre = {
    "Fiction": ["B001", "B004"],
    ...
}
```

This is printed in a friendly format so users can browse all books.

---

### 4. 👥 User Data

Each user is stored in a **dictionary** with their name as the key and a list of borrowed book IDs as the value.

Example:

```python
users = {
    "alice": ["B001", "B005"],
    "bob": []
}
```

---

## 🔁 Main Interactions

After listing books and users:

### Step 1: Login

The program asks you to enter your name. If you’re registered, it welcomes you and shows your borrowed books.

### Step 2: Borrow or Return

You’re asked whether you want to `"borrow"` or `"return"` a book.

### Step 3A: Borrowing

- All available books are shown grouped by genre.
- You type the book ID you want to borrow.
- If it’s valid and not already borrowed, the book is added to your list.

### Step 3B: Returning

- Your borrowed books are displayed.
- You choose a book ID to return.
- If valid, the book is removed from your list and a confirmation is shown.

---

## ⚠️ Error Handling

The program handles:

- Users not found (asks them to register)
- Invalid book IDs
- Trying to borrow a book already borrowed
- Trying to return a book not currently borrowed

---

## 🧠 Concepts Practiced

| Python Concept | Usage                                |
| -------------- | ------------------------------------ |
| `dict`         | Storing books, users, and genres     |
| `list`         | Tracking borrowed books per user     |
| `tuple`        | Storing book details                 |
| `set`          | Managing unique genres               |
| `input()`      | Accepting user interaction           |
| `if/else`      | Making decisions based on conditions |
| `for` loop     | Printing books and user lists        |
| `str.lower()`  | Handling case-insensitive names      |

---

## 🚀 How to Run

1. Open the code in a Python IDE or Jupyter Notebook.
2. Run the script.
3. Follow the on-screen prompts.

---

## 🔧 Ideas for Expansion

- Add registration for new users
- Save and load data using JSON files
- Track number of available copies per book
- Add due dates and overdue notices

---

👩‍💻 Happy coding and borrowing!
