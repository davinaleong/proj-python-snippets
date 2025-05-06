# 👤 User Management in Davina's Library

This section of the Python program manages the **library users** and shows what books they've borrowed. It interacts with users by asking for their name and displaying their borrowed books if they're registered.

---

## 📇 User Data

```python
users = {
    "alice": ["B001", "B005"],
    "bob": [],
    "charlie": ["B007"],
    "diana": ["B003", "B010"],
    "ethan": ["B006"]
}
```

- This is a **dictionary** where each key is a **user name**.
- Each user has a **list of book IDs** they’ve borrowed.
- If the list is empty (`[]`), the user hasn't borrowed any books yet.

> Think of it like each user has a folder with a list of borrowed book IDs inside.

---

## 👀 Show All Users

```python
print(f"--- Users of {library} ---")
for user in users:
    print(f"- {user}")
```

- Prints out a list of all users in the system.
- Helpful for testing or verifying who is registered.

---

## 🧾 User Login and Borrowed Books Check

```python
user = input("Please enter your name:")
user_input = str(user).lower()
```

- Asks the user to type their name.
- Converts the name to lowercase so the check is case-insensitive (e.g., `Alice` = `alice`).

---

### ✅ If the User Exists

```python
if user_input in users:
    print(f"Welcome back, {user}:")
```

- Checks if the entered name is already in the `users` dictionary.

---

### 📚 Show Borrowed Books

```python
borrowed_book_uuids = users[user_input]

if borrowed_book_uuids:
    print("You have borrowed the following books:")

    for borrowed_book_uuid in borrowed_book_uuids:
        (title, author, genre) = books[borrowed_book_uuid]
        print(f"  - {borrowed_book_uuid}: {title} by {author}, {genre}")
```

- Retrieves the list of book IDs the user has borrowed.
- For each book ID, it looks up the **book title, author, and genre** from the `books` dictionary.
- Prints the full book info in a friendly format.

---

### ❌ If the User is Not Found

```python
else:
    print(f"User '{user}' not found. Please register first.")
```

- This message is shown when someone who isn't in the system tries to log in.

---

## 💡 Summary

This code helps beginners understand:

| Concept        | Purpose                                            |
| -------------- | -------------------------------------------------- |
| `dict`         | To store users and what they’ve borrowed           |
| `list`         | To keep track of each user’s borrowed books        |
| `input()`      | To get the user’s name                             |
| `for` loop     | To print lists of users and books                  |
| `if` statement | To check if the user exists and what they borrowed |
