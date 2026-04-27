"""
Реалізація патерну "Спостерігач" (Observer) для системи повідомлення клієнтів про появу товару.
"""

from abc import ABC, abstractmethod


class Subject(ABC):
    """Інтерфейс Суб'єкт."""

    @abstractmethod
    def attach(self, observer):
        """Підписати спостерігача."""

    @abstractmethod
    def detach(self, observer):
        """Відписати спостерігача."""

    @abstractmethod
    def notify(self):
        """Сповістити всіх підписаних спостерігачів."""


class Observer(ABC):
    """Інтерфейс Спостерігач."""

    @abstractmethod
    def update(self, product):
        """Отримати сповіщення про оновлення продукту."""


class Product(Subject):
    """Товар, який може повідомляти спостерігачів."""

    def __init__(self, name: str, quantity: int = 0):
        self.name = name
        self.quantity = quantity
        self._observers = []

    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def set_quantity(self, new_quantity: int):
        """Оновлює кількість товару. Якщо він знову з’явився — сповіщає клієнтів."""
        was_out_of_stock = self.quantity == 0
        self.quantity = new_quantity

        if was_out_of_stock and self.quantity > 0:
            self.notify()


class Customer(Observer):
    """Клієнт, який отримує повідомлення про товари."""

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def update(self, product: Product):
        print(
            f"Привіт, {self.name}! Товар '{product.name}' знову в наявності "
            f"({product.quantity} шт). Поспішайте зробити замовлення!"
        )


# --- Демонстрація ---
def main():
    """Демонстрація роботи патерну Спостерігач."""
    phone = Product("Смартфон", 0)
    laptop = Product("Ноутбук", 0)

    alice = Customer("Аліса", "alice@example.com")
    bob = Customer("Боб", "bob@example.com")
    charlie = Customer("Чарлі", "charlie@example.com")

    phone.attach(alice)
    phone.attach(bob)
    laptop.attach(charlie)
    laptop.attach(bob)

    print("\n📦 Смартфон поповнено:")
    phone.set_quantity(10)

    print("\n📦 Ноутбук поповнено:")
    laptop.set_quantity(5)

    print("\n❌ Боб відписався від повідомлень про ноутбук")
    laptop.detach(bob)

    print("\n📦 Ноутбук знову поповнено:")
    laptop.set_quantity(3)


if __name__ == "__main__":
    main()
