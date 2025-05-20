def validate_args(func):
    def wrapper(self, title, author, pages, year):
        if not title:
            raise ValueError("Title must be provided")
        if not author:
            raise ValueError("Author must be provided")
        if pages <= 0:
            raise ValueError("Pages must be positive")
        if year <= 0:
            raise ValueError("Year must be positive")
        return func(self, title, author, pages, year)
    return wrapper


class Book:
    @validate_args
    def __init__(self, title, author, pages, year):
        self.__title = title
        self.author = author
        self.pages = pages
        self.year = year

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        if new_title != self.__title:
            self.__title = new_title
        else:
            raise ValueError("You must provide a new title, not the same one")

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (self.title, self.pages, self.year, self.author) == (other.title, other.pages, other.year, other.author)

    def __hash__(self):
        return hash((self.title, self.pages, self.year, self.author))

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages}, {self.year})"
