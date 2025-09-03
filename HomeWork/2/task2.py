"""Програма для моделювання графічних об'єктів."""


class GraphicObject:
    """Базовий графічний об'єкт."""

    def draw(self):
        """Намалювати графічний об'єкт."""
        print("Малюється графічний об'єкт.")


class Rectangle(GraphicObject):
    """Прямокутник."""

    def draw(self):
        """Намалювати прямокутник."""
        print("Малюється прямокутник.")


class Clickable:
    """Інтерфейс для об'єктів, що реагують на кліки."""

    def on_click(self):
        """Обробка натискання миші."""
        print("Об'єкт обробляє натискання миші.")


class Button(Rectangle, Clickable):
    """Кнопка."""

    def draw(self):
        """Намалювати кнопку."""
        print("Малюється кнопка.")


def main():
    """Основна логіка програми."""
    btn = Button()
    rect = Rectangle()

    btn.draw()
    btn.on_click()
    rect.draw()


if __name__ == "__main__":
    main()
