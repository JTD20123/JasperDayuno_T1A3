from book_functions import add_book, search_books, load_catalog_from_json,  view_catalog


catalog = []

def main():
    print("Welcome to the Book Catalog App")
    while True:
        print("1. Add a Book")
        print("2. Search Books")
        print("3. View Catalog")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            search_books()
        elif choice == '3':
            view_catalog()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    load_catalog_from_json() #  ensures that when the program starts, any previously saved catalog data is read and made available for use.
    main()
