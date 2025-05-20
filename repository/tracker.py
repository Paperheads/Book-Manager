from models.book import Book


class BookRepository:
    @staticmethod
    def to_dict(book: Book) -> dict:
        if not isinstance(book, Book):
            raise TypeError("Expected a Book instance")
        return {
            "title": book.title,
            "author": book.author,
            "pages": book.pages,
            "year": book.year
        }

    @staticmethod
    def from_dict(data: dict) -> Book:
        return Book(
            title=data.get("title"),
            author=data.get("author"),
            pages=data.get("pages"),
            year=data.get("year")
        )

import json
import os
class JSONFileManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = []

    def __enter__(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r', encoding='utf-8') as f:
                try:
                    self.data = json.load(f)
                except json.JSONDecodeError:
                    self.data = []
        else:
            self.data = []
        return self

    def save(self):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=4)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save()