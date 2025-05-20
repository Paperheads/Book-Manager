from models.book import Book
from repository.tracker import BookRepository
from repository.tracker import JSONFileManager


class BookService:

    def __init__(self, filepath: str):
        self.filepath = filepath

    def add_book(self, book: Book):
        with JSONFileManager(self.filepath) as file:
            book_dict = BookRepository.to_dict(book)
            file.data.append(book_dict)

    def get_all_books(self) -> list[Book]:
        with JSONFileManager(self.filepath) as file:
            return [BookRepository.from_dict(entry) for entry in file.data]

    def find_by_author(self, author_name: str) -> list[Book]:
        books = self.get_all_books()
        return [book for book in books if book.author == author_name]

    def delete_by_title(self, title: str):
        with JSONFileManager(self.filepath) as file:
            file.data = [entry for entry in file.data if entry.get("title") != title]

    def get_sorted_books(self, key: str, reverse: bool = False) -> list[Book]:
        with JSONFileManager(self.filepath) as file:
            sorted_data = sorted(
                file.data,
                key=lambda x: x.get(key),
                reverse=reverse
            )
            return [BookRepository.from_dict(entry) for entry in sorted_data]