"""Модуль із класом Book, що демонструє використання спеціальних методів."""


class Book:
    """Клас, що описує книгу (назва, автор, кількість сторінок)."""

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """Виведення об’єкта через print()."""
        return f"Книга: {self.title}, Автор: {self.author}, {self.pages} стор."

    def __len__(self):
        """Повертає кількість сторінок книги."""
        return self.pages

    def __lt__(self, other):
        """Порівняння книг за кількістю сторінок."""
        return self.pages < other.pages

    def __add__(self, other):
        """Об’єднання двох книг у 'збірник'."""
        return Book(
            title=f"{self.title} + {other.title}",
            author=f"{self.author} та {other.author}",
            pages=self.pages + other.pages,
        )


book1 = Book("Місто", "Валер'ян Підмогильний", 300)
book2 = Book("Тигролови", "Іван Багряний", 250)

print(book1)
print(len(book1))
print(book1 < book2)
print(book1 + book2)
