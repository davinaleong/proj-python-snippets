library = "Davina's Library"
print(f"=== Welcome to {library} ===")

# books data structure > dictionary { book uuid }
# book item data structure > tuple: (title, author, genre)
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

# genres data structure > dictionary { genre name }
genres = {
    "Fiction",
    "Dystopian",
    "Classic",
    "Non-fiction",
    "Programming",
    "Fantasy",
    "Science",
    "Biography",
    "Thriller"
}

# books_by_genre > dictionary { book uuid }
books_by_genre = {}

print("--- Books Sorted by Genre ---")
for book_id, (title, author, genre) in books.items():
    if genre not in books_by_genre:
        books_by_genre[genre] = []
    books_by_genre[genre].append(book_id)

for genre, book_uuids in books_by_genre.items():
    print(f"\n📚 Genre: {genre}")
    for book_uuid in book_uuids:
        title, author, _ = books[book_uuid]
        print(f"  - {book_uuid}: {title} by {author}")
