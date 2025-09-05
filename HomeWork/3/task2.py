"""Модуль з класами мов (English, Spanish)."""


class English:
    """Клас для англійської мови."""

    def greeting(self) -> str:
        """Привітання англійською мовою."""
        return "Hello, friend!"


class Spanish:
    """Клас для іспанської мови."""

    def greeting(self) -> str:
        """Привітання іспанською мовою."""
        return "¡Hola, amigo!"


def hello_friend():
    """Створюємо об'єкти двох мов і викликаємо їхні методи greeting()."""
    eng = English()
    esp = Spanish()

    print(eng.greeting())
    print(esp.greeting())


if __name__ == "__main__":
    hello_friend()
