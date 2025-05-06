# users data structure > dictionary { user name }
# user item data structure > list: [book uuid]
users = {
    "alice": ["B001", "B005"],          # Borrowed: The Alchemist, Sapiens
    "bob": [],                          # No borrowed books
    "charlie": ["B007"],               # Borrowed: The Hobbit
    "diana": ["B003", "B010"],         # Borrowed: To Kill a Mockingbird, The Silent Patient
    "ethan": ["B006"]                  # Borrowed: Python Crash Course
}

# Print out the users of the library management system
print(f"--- Users of {library} ---")
for user in users:
    print(f"- {user}")

user = input("Please enter your name:")
user_input = str(user).lower()

if user_input in users:
    print(f"Welcome back, {user}:")

    borrowed_book_uuids = users[user_input]

    if borrowed_book_uuids:
        print("You have borrowed the following books:")

        for borrowed_book_uuid in borrowed_book_uuids:
            (title, author, genre) = books[borrowed_book_uuid]
            print(f"  - {borrowed_book_uuid}: {title} by {author}, {genre}")
else:
    print(f"User '{user}' not found. Please register first.")