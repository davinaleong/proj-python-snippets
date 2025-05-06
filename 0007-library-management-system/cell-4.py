# === Davina's Library System ===
library = "Davina's Library"
print(f"=== Welcome to {library} ===")

# Book database: book_id => (title, author, genre)
books = {
    "B001": ("The Alchemist", "Paulo Coelho", "Fiction"),
    "B002": ("1984", "George Orwell", "Dystopian"),
    "B003": ("To Kill a Mockingbird", "Harper Lee", "Classic"),
    "B004": ("The Great Gatsby", "F. Scott Fitzgerald", "Classic"),
    "B005": ("Sapiens", "Yuval Noah Harari", "Non-fiction"),
    "B006": ("Python Crash Course", "Eric Matthes", "Programming"),
    "B007": ("The Hobbit", "J.R.R. Tolkien", "Fantasy"),
    "B008": ("A Brief History of Time", "Stephen Hawking", "Science"),
    "B009": ("Becoming", "Michelle Obama", "Biography"),
    "B010": ("The Silent Patient", "Alex Michaelides", "Thriller")
}

# Users and their borrowed book IDs
users = {
    "alice": ["B001", "B005"],
    "bob": [],
    "charlie": ["B007"],
    "diana": ["B003", "B010"],
    "ethan": ["B006"]
}

# Group books by genre
books_by_genre = {}
for book_id, (_, _, genre) in books.items():
    books_by_genre.setdefault(genre, []).append(book_id)

# Show all books grouped by genre
def show_all_books():
    print("\n--- Books Sorted by Genre ---")
    for genre, book_ids in books_by_genre.items():
        print(f"\n📚 {genre}")
        for book_id in book_ids:
            title, author, _ = books[book_id]
            print(f"  - {book_id}: {title} by {author}")

# Show a user's borrowed books
def show_borrowed_books(username):
    borrowed = users[username]
    if not borrowed:
        print("You haven't borrowed any books yet.")
    else:
        print("You have borrowed the following books:")
        for book_id in borrowed:
            title, author, genre = books[book_id]
            print(f"  - {book_id}: {title} by {author}, {genre}")

# Borrow a book
def borrow_book(username):
    show_all_books()
    book_id = input("\nWhich book would you like to borrow? ").upper()
    if book_id not in books:
        print("That book ID does not exist.")
    elif book_id in users[username]:
        print("You've already borrowed this book.")
    else:
        users[username].append(book_id)
        title, author, genre = books[book_id]
        print(f"You borrowed: {book_id}: {title} by {author} ({genre})")

# Return a book
def return_book(username):
    borrowed = users[username]
    if not borrowed:
        print("You haven't borrowed any books yet.")
        return

    show_borrowed_books(username)
    book_id = input("\nWhich book would you like to return? ").upper()
    if book_id in borrowed:
        borrowed.remove(book_id)
        title, author, genre = books[book_id]
        print(f"You returned: {book_id}: {title} by {author} ({genre})")
    else:
        print("You haven't borrowed that book.")

# === Start Program ===

# Show registered users
print("\n--- Registered Users ---")
for name in users:
    print(f"- {name}")

# Login
username_input = input("\nPlease enter your name: ").strip().lower()

if username_input in users:
    print(f"\nWelcome back, {username_input.capitalize()}!")
    show_borrowed_books(username_input)

    action = input("\nWould you like to borrow or return a book? (borrow/return): ").lower()
    if action == "borrow":
        borrow_book(username_input)
    elif action == "return":
        return_book(username_input)
    else:
        print("Invalid action. Please type 'borrow' or 'return'.")
else:
    print(f"User '{username_input}' not found. Please register first.")
