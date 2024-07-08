from book_functions import add_book
import json

catalog = []

def main():
    print("Welcome to the Book Catalog App")
    while True:
        print("1. Add a Book")
        print("2. Search and Sort Books")
        print("3. View Catalog")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            search_books()
        elif choice == '3':
            display_books()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
