import json
from book import Book

catalog = []

def validate_year(year):
    # Example: Publication year should be a valid year (within a reasonable range)
    try:
        year = int(year)
        return year >= 1900 and year <= 2100
    except ValueError:
        return False

# add a new book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    genre = input("Enter genre: ")
    publication_year = input("Enter publication year: ")
    
    while not validate_year(publication_year):
        print("Invalid year format. Please enter a valid year.")
        publication_year = input("Enter publication year: ")

    new_book = Book(title, author, genre, publication_year)
    catalog.append(new_book)
    
    save_books_to_json()  # Save catalog to JSON file

    print("Book added successfully!\n")

def save_books_to_json():
    # Convert each Book object to a dictionary representation
    books_data = []
    for book in catalog:
        book_data = {
            'title': book.title,
            'author': book.author,
            'genre': book.genre,
            'publication_year': book.publication_year
        }
        books_data.append(book_data)
    
    # Save to JSON file
    with open('catalog.json', 'w') as f:
        json.dump(books_data, f, indent=4)

#search books from database
def search_books_by_title(title):
    found_books = [book for book in catalog if title.lower() in book.title.lower()]
    return found_books

def search_books_by_author(author):
    found_books = [book for book in catalog if author.lower() in book.author.lower()]
    return found_books

def search_books_by_genre(genre):
    found_books = [book for book in catalog if genre.lower() in book.genre.lower()]
    return found_books

def display_search_menu():
    print("Search Books:")
    print("1. By Title")
    print("2. By Author")
    print("3. By Genre")
    print("4. Back to Main Menu")
