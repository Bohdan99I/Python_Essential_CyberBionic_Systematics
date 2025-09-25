"""Проста реалізація класів Book і Library з можливістю додавання та видалення книг."""


class Book:
    """Клас для представлення книги."""

    def __init__(self, title: str, author: str, year: int, genre: str):
        """Ініціалізація книги з назвою, автором, роком та жанром."""
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        """Повертаємо рядкове представлення книги."""
        return f"'{self.title}' — {self.author}, {self.year} ({self.genre})"


class Library:
    """Клас бібліотеки з ітератором."""

    def __init__(self):
        """Створюємо порожню бібліотеку."""
        self.books = []
        self._index = 0

    def __iter__(self):
        """Повертаємо ітератор для перебору книг."""
        self._index = 0
        return self

    def __next__(self):
        """Повертаємо наступну книгу з бібліотеки або StopIteration."""
        if self._index < len(self.books):
            book = self.books[self._index]
            self._index += 1
            return book
        raise StopIteration

    def __len__(self):
        """Повертаємо кількість книг у бібліотеці."""
        return len(self.books)

    def __str__(self):
        """Повертаємо список усіх книг або повідомлення про порожню бібліотеку."""
        return (
            "\n".join(str(book) for book in self.books)
            if self.books
            else "Бібліотека порожня"
        )

    def add_book(self, book: Book):
        """Додаємо книгу до бібліотеки."""
        self.books.append(book)

    def remove_book(self, title: str):
        """Видаляємо книгу з бібліотеки за назвою."""
        self.books = [b for b in self.books if b.title != title]


def main():
    """Меню для взаємодії користувача з бібліотекою."""
    lib = Library()

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Додати книгу")
        print("2. Видалити книгу")
        print("3. Показати всі книги")
        print("4. Вихід")

        choice = input("Оберіть дію: ")

        if choice == "1":
            title = input("Введіть назву книги: ")
            author = input("Введіть автора: ")
            year = input("Введіть рік видання: ")
            genre = input("Введіть жанр: ")

            book = Book(title, author, year, genre)
            lib.add_book(book)
            print("✅ Книгу додано!")

        elif choice == "2":
            title = input("Введіть назву книги для видалення: ")
            lib.remove_book(title)
            print("🗑 Книгу видалено (якщо була у бібліотеці).")

        elif choice == "3":
            print("\n📚 У бібліотеці:")
            print(lib)

        elif choice == "4":
            print("👋 Вихід з програми.")
            break

        else:
            print("❌ Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
