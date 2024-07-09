import json
from book import Book

catalog = []

# Function to validate publication year
def validate_year(year):
    # Example: Publication year should be a valid year (within a reasonable range)
    try:
        year = int(year)
        return year >= 1900 and year <= 2100
    except ValueError:
        return False
    
# Function to save catalog to JSON file
def save_books_to_json():
    # Saves the catalog of books to a JSON file named 'catalog.json'
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
# Function to load catalog from JSON file
def load_catalog_from_json():
    global catalog
    try:
        with open('catalog.json', 'r') as f:
            catalog_data = json.load(f)
            catalog = [Book(**book_data) for book_data in catalog_data]
    except FileNotFoundError:
        print("Catalog file not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

# Function to add a new book to catalog
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


# Function to search for books in catalog

def search_books():
    print("Search Books:")
    print("1. By Title")
    print("2. By Author")
    print("3. By Genre")
    print("4. By Publication Year")
    print("5. Back to Main Menu")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        title = input("Enter title to search for: ")
        found_books = [book for book in catalog if title.lower() in book.title.lower()]
        display_search_results(found_books)
    
    elif choice == '2':
        author = input("Enter author to search for: ")
        found_books = [book for book in catalog if author.lower() in book.author.lower()]
        display_search_results(found_books)
    
    elif choice == '3':
        genre = input("Enter genre to search for: ")
        found_books = [book for book in catalog if genre.lower() in book.genre.lower()]
        display_search_results(found_books)
    
    elif choice == '4':
        publication_year = input("Enter publication year to search for: ")
        while not validate_year(publication_year):
            print("Invalid year format. Please enter a valid year.")
            publication_year = input("Enter publication year: ")
        
        found_books = [book for book in catalog if publication_year == book.publication_year]
        display_search_results(found_books)
    
    elif choice == '5':
        return       # Return to main menu
    
    else:
        print("Invalid choice. Please enter a number between 1 and 5.\n")

# Function to display search results
def display_search_results(found_books):
    if found_books:
        print("\nResults:")
        for book in found_books:
            print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Publication Year: {book.publication_year}")
        print()
    else:
        print("No books found.\n")

def display_books():
    load_catalog_from_json()
    if catalog:
        print("\nCatalog:")
        for idx, book in enumerate(catalog, start=1):
            read_status = "Read" if book.is_read else "Unread"
            print(f"{idx}. Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Publication Year: {book.publication_year}, Status: {read_status}")
        print()
    else:
        print("Catalog is empty.\n")

def view_catalog():
    if catalog:
        print("Books in Catalog:")
        for index, book in enumerate(catalog):
            print(f"{index + 1}. Title: {book.title}")
            print(f"   Author: {book.author}")
            print(f"   Genre: {book.genre}")
            print("--------------------")
        
        choice = input("Enter the number of the book you want to remove, or '0' to cancel: ")
        if choice.isdigit():
            index_to_remove = int(choice) - 1
            if 0 <= index_to_remove < len(catalog):
                removed_book = catalog.pop(index_to_remove)
                print(f"Removed book: {removed_book.title}")
                save_books_to_json()  # Save catalog to JSON file after removal
            elif index_to_remove == -1:
                print("Canceled removal.")
            else:
                print("Invalid index. No book removed.")
        else:
            print("Invalid input. No book removed.")

    else:
        print("No books found in the catalog.")