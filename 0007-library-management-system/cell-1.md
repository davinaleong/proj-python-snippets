# 📚 Welcome to Davina's Library Code Walkthrough

This Python program simulates a small library system. It organizes a collection of books by their genres and displays them in an easy-to-read format.

---

## 🏷️ Library Name

```python
library = "Davina's Library"
print(f"=== Welcome to {library} ===")
```

We start by setting the name of the library and printing a welcome message. The `{library}` part gets replaced with the actual name.

---

## 📖 Book Collection

```python
books = {
    "B001": ("The Alchemist", "Paulo Coelho", "Fiction"),
    ...
}
```

- This is a **dictionary** where each book has a **unique ID** like `"B001"`.
- Each book's value is a **tuple** containing:
  - The title of the book
  - The author’s name
  - The genre it belongs to

> Think of it like a library record card for each book.

---

## 🗂️ Genres

```python
genres = {
    "Fiction",
    "Dystopian",
    ...
}
```

This is a **set** of all the different book genres. Sets are used when we only want unique values (no duplicates).

---

## 🧩 Grouping Books by Genre

```python
books_by_genre = {}
```

We create an **empty dictionary** to store books sorted by genre.

---

### 🔄 Looping Through the Books

```python
for book_id, (title, author, genre) in books.items():
    if genre not in books_by_genre:
        books_by_genre[genre] = []
    books_by_genre[genre].append(book_id)
```

- This loop checks each book’s genre.
- If the genre isn’t in the dictionary yet, it creates a new list for that genre.
- Then, it adds the book ID to the list under the correct genre.

---

## 📋 Displaying the Books

```python
for genre, book_uuids in books_by_genre.items():
    print(f"\n📚 Genre: {genre}")
    for book_uuid in book_uuids:
        title, author, _ = books[book_uuid]
        print(f"  - {book_uuid}: {title} by {author}")
```

This section prints each genre followed by a list of books under that category, including their:

- Book ID
- Title
- Author

---

### ✅ Example Output

```
📚 Genre: Fiction
  - B001: The Alchemist by Paulo Coelho

📚 Genre: Classic
  - B003: To Kill a Mockingbird by Harper Lee
  - B004: The Great Gatsby by F. Scott Fitzgerald
```

---

## 💡 Summary

This code teaches:

- How to store and access book info using dictionaries and tuples
- How to avoid duplicate genres using a set
- How to organize data using loops and nested structures

Perfect for beginners building a simple but structured Python project!
