print(f"--- {library} Borrow/Return System ---")

# actions data structure > tuple
actions = ("borrow", "return")

user = input("Please enter your name:")
user_input = str(user).lower()

if user_input in users:
    user = users[user_input]

    print(f"Would you like to borrow or return a book?")
    print(f"Available options: {actions}")
    action = input("Please enter your choice (borrow/return): ").lower()

    # if user wants to borrow a book
    if action == actions[0]:
        print("Available books:")
        
        for genre, book_uuids in books_by_genre.items():
            print(f"\n📚 Genre: {genre}")
            for book_uuid in book_uuids:
                title, author, _ = books[book_uuid]
                print(f"  - {book_uuid}: {title} by {author}")

        book_uuid = input("Which book would you like to borrow?").upper()

        if book_uuid in books and book_uuid not in users[user_input]:
            users[user_input].append(book_uuid)

            title, author, genre = books[book_uuid]
            print(f"You borrowed '{book_uuid}: {title} by {author}, {genre}'")
        else:
            print(f"Book '{book_uuid}' not found.")
      
    # if user wants to return a book
    elif action == actions[1]:
        borrowed_book_uuids = users[user_input]
    
        if borrowed_book_uuids:
            print("You have borrowed the following books:")
    
            for borrowed_book_uuid in borrowed_book_uuids:
                (title, author, genre) = books[borrowed_book_uuid]
                print(f"  - {borrowed_book_uuid}: {title} by {author}, {genre}")

            book_uuid = input("Which book would you like to return?").upper()

            if book_uuid in borrowed_book_uuids:
                borrowed_book_uuids.remove(book_uuid)
                users[user_input] = borrowed_book_uuids
                (title, author, genre) = books[book_uuid]
                print(f"You returned: '{book_uuid}: {title} by {author}, {genre}")

                if borrowed_book_uuids:
                    print("You have following books left:")
        
                    for borrowed_book_uuid in borrowed_book_uuids:
                        (title, author, genre) = books[borrowed_book_uuid]
                        print(f"  - {borrowed_book_uuid}: {title} by {author}, {genre}")
            else:
                print(f"Book '{book_uuid}' not found.")
        else:
            print("You haven't borrowed any books yet.")
    else:
        print(f"Invalid action '{action}'.")
else:
    print(f"User '{user}' not found. Please register first.")