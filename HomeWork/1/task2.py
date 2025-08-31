"""Модуль із класами Book та Review для роботи з книгами й відгуками."""


class Review:
    """Клас, що описує відгук до книги (автор відгуку, текст, оцінка)."""

    def __init__(self, reviewer, text, rating):
        self.reviewer = reviewer
        self.text = text
        self.rating = rating

    def __str__(self):
        return f"Відгук від {self.reviewer} ({self.rating}/5): {self.text}"

    def __repr__(self):
        return (
            f"Review(reviewer={self.reviewer!r}, "
            f"text={self.text!r}, rating={self.rating!r})"
        )


class Book:
    """Клас, що описує книгу з полем для списку відгуків."""

    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        self.reviews = []  # список відгуків

    def add_review(self, review):
        """Додає відгук (об’єкт Review) до списку відгуків книги."""
        if isinstance(review, Review):
            self.reviews.append(review)
        else:
            raise ValueError("Відгук має бути об’єктом класу Review")

    def __str__(self):
        info = f"📖 «{self.title}» — {self.author}, {self.year}, жанр: {self.genre}\n"
        if self.reviews:
            info += "Відгуки:\n"
            for r in self.reviews:
                info += f"  - {r}\n"
        else:
            info += "Відгуків ще немає."
        return info

    def __repr__(self):
        return (
            f"Book(author={self.author!r}, title={self.title!r}, "
            f"year={self.year!r}, genre={self.genre!r})"
        )


book1 = Book("Джордж Орвелл", "1984", 1949, "антиутопія")
review1 = Review("Андрій", "Дуже сильна книга, змушує замислитися.", 5)
review2 = Review("Марія", "Трохи похмуро, але цікаво.", 4)

book1.add_review(review1)
book1.add_review(review2)

print(book1)
