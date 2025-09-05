"""Модуль із прикладом використання classmethod."""


class Base:
    """Базовий клас з методом method()."""

    @classmethod
    def method(cls):
        """Виводимо повідомлення з базового класу."""
        print("Hello from Base")


class Child(Base):
    """Клас-нащадок, який перевизначає метод method()."""

    @classmethod
    def method(cls):
        """Виводимо повідомлення з дочірнього класу."""
        print("Hello from Child")


if __name__ == "__main__":
    # Виклик методу через клас
    Base.method()
    Child.method()

    # Виклик методу через екземпляр
    base_obj = Base()
    child_obj = Child()

    base_obj.method()
    child_obj.method()
