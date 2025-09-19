"""
Сервіс скорочення посилань з чітким розділенням:
- core.py: логіка роботи (інтерфейс для роботи з базою)
- ui_console.py: консольний інтерфейс (представлення)
"""

import shelve
import os


class LinkService:
    """Сервіс скорочення посилань з збереженням бази на диску."""

    def __init__(self, db_filename="short_links.db"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_filename = os.path.join(base_dir, db_filename)

    def add_link(self, original_url, short_name):
        """Додає посилання до бази даних."""
        with shelve.open(self.db_filename) as db:
            if short_name in db:
                return False, f"Назва '{short_name}' вже використовується."
            db[short_name] = original_url
            return True, f"Посилання додано: {short_name} -> {original_url}"

    def get_link(self, short_name):
        """Повертає початкове посилання за короткою назвою."""
        with shelve.open(self.db_filename) as db:
            url = db.get(short_name)
            if url:
                return True, url
            return False, f"Посилання з назвою '{short_name}' не знайдено."

    def get_all_links(self):
        """Повертає всі посилання у базі даних."""
        with shelve.open(self.db_filename) as db:
            if not db:
                return False, "База порожня."
            return True, dict(db)


class ConsoleUI:
    """Консольний інтерфейс."""

    def __init__(self, service: LinkService):
        self.service = service

    def run(self):
        """Запускає консольний інтерфейс."""
        while True:
            print("\nСервіс скорочення посилань")
            print("1 - Додати посилання")
            print("2 - Отримати посилання")
            print("3 - Показати всі посилання")
            print("0 - Вийти")

            choice = input("Ваш вибір: ")

            if choice == "1":
                url = input("Введіть початкове посилання: ")
                name = input("Введіть коротку назву: ")
                success, message = self.service.add_link(url, name)
                print(message)
            elif choice == "2":
                name = input("Введіть коротку назву: ")
                success, result = self.service.get_link(name)
                if success:
                    print(f"Початкове посилання: {result}")
                else:
                    print(result)
            elif choice == "3":
                success, result = self.service.get_all_links()
                if success:
                    print("Усі посилання:")
                    for name, url in result.items():
                        print(f"{name} -> {url}")
                else:
                    print(result)
            elif choice == "0":
                print("Вихід з програми...")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    link_service = LinkService()
    ui = ConsoleUI(link_service)
    ui.run()
