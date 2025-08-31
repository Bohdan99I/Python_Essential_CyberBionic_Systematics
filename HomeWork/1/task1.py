"""Модуль із класом Book, який описує книгу."""


class Book:
    """Клас, що описує книгу з атрибутами: автор, назва, рік та жанр."""

    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

    def __repr__(self):
        return (
            f"Book(author='{self.author}', title='{self.title}', "
            f"year={self.year}, genre='{self.genre}')"
        )

    def __str__(self):
        return f"'{self.title}' ({self.year}), {self.author} — жанр: {self.genre}"


book1 = Book("Джордж Орвелл", "1984", 1949, "Антиутопія")
book2 = Book("Дж. К. Ролінг", "Гаррі Поттер і філософський камінь", 1997, "Фентезі")
book3 = Book("Френсіс Скотт Фіцджеральд", "Великий Ґетсбі", 1925, "Роман")

print(book1)
print(book2)
print(book3)

print(repr(book1))
