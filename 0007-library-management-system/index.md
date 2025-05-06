# 📚 Simple Library Management System

This is a beginner-friendly project made with **Python in Jupyter Notebook**. It helps you practice using:

- ✅ **Lists**
- ✅ **Tuples**
- ✅ **Sets**
- ✅ **Dictionaries**
- ✅ **Nested data** (like a list inside a dictionary)

---

## 🎯 What This Project Does

You’ll build a small system to:

1. Store book info like title and author
2. Track users and which books they borrowed
3. Show available books
4. Let users borrow or return books
5. Learn core Python data types

---

## 🛠️ What You’ll Learn

| Python Concept | What You’ll Use It For                |
| -------------- | ------------------------------------- |
| List           | To track borrowed books               |
| Tuple          | To store book details (title, author) |
| Set            | To collect unique genres              |
| Dictionary     | To store books and user info          |
| Nested data    | A dictionary with lists or tuples     |

---

## 📋 Steps in the Notebook

1. **Create a book list** using a dictionary:

```python
books = {
  "B001": ("The Alchemist", "Paulo Coelho", "Fiction"),
  "B002": ("1984", "George Orwell", "Dystopian")
}
```

2. **Track users** and what they borrowed:

```python
users = {
  "alice": ["B001"],
  "bob": []
}
```

3. **Get unique genres** using a set:

```python
genres = set(book[2] for book in books.values())
```

4. **Make simple functions**:

- View all books
- Borrow a book
- Return a book

5. **Add a menu** using a `while` loop:

```python
while True:
    print("1. View Books\n2. Borrow\n3. Return\n4. Exit")
    choice = input("Choose an option: ")
```
