from models.book import Book
from services.book_service import BookService


class BookCLI:
    def __init__(self, filepath: str):
        self.service = BookService(filepath)
        self.commands = {
            "1": self.add_book,
            "2": self.show_all_books,
            "3": self.find_books_by_author,
            "4": self.delete_book_by_title,
            "5": self.sort_books,
            "0": self.exit_program
        }
        self.running = True

    def display_menu(self):
        print("\nBook Manager CLI")
        print("─" * 25)
        print("1. Add a new book")
        print("2. Show all books")
        print("3. Find books by author")
        print("4. Delete book by title")
        print("5. Sort books by key")
        print("0. Exit")

    def run(self):
        while self.running:
            self.display_menu()
            choice = input("Select an option: ").strip()
            action = self.commands.get(choice)
            if action:
                action()
            else:
                print("!Invalid option. Please try again.")

    def add_book(self):
        try:
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            pages = int(input("Pages: ").strip())
            year = int(input("Year: ").strip())
            book = Book(title, author, pages, year)
            self.service.add_book(book)
            print("Book added successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def show_all_books(self):
        books = self.service.get_all_books()
        if not books:
            print("No books found.")
        for book in books:
            print(f"• {book}")

    def find_books_by_author(self):
        author = input("Author name: ").strip()
        results = self.service.find_by_author(author)
        if results:
            print(f"\nBooks by '{author}':")
            for book in results:
                print(f"• {book}")
        else:
            print("No books found for this author.")

    def delete_book_by_title(self):
        title = input("Title to delete: ").strip()
        self.service.delete_by_title(title)
        print(f"Book with title '{title}' deleted (if it existed).")

    def sort_books(self):
        key = input("Sort by (title, author, pages, year): ").strip()
        reverse = input("Descending? (y/n): ").strip().lower() == "y"
        try:
            books = self.service.get_sorted_books(key, reverse)
            print(f"\nBooks sorted by '{key}':")
            for book in books:
                print(f"• {book}")
        except Exception as e:
            print(f"Sort error: {e}")

    def exit_program(self):
        print("Goodbye!")
        self.running = False
