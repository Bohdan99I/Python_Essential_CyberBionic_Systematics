"""
Сервіс скорочення посилань з збереженням бази на диску.
"""

import shelve
import os

# Отримуємо шлях до директорії, де лежить сам скрипт
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILENAME = os.path.join(BASE_DIR, "short_links.db")


def add_link(original_url, short_name):
    """Додає посилання до бази даних."""
    with shelve.open(DB_FILENAME) as db:
        if short_name in db:
            print(f"Назва '{short_name}' вже використовується. Виберіть іншу.")
        else:
            db[short_name] = original_url
            print(f"Посилання додано: {short_name} -> {original_url}")


def get_link(short_name):
    """Повертає початкове посилання за короткою назвою."""
    with shelve.open(DB_FILENAME) as db:
        url = db.get(short_name)
        if url:
            return url
        else:
            print(f"Посилання з назвою '{short_name}' не знайдено.")
            return None


def show_all_links():
    """Виводить всі посилання у базі даних."""
    with shelve.open(DB_FILENAME) as db:
        if not db:
            print("База порожня.")
        else:
            print("Усі посилання:")
            for name, url in db.items():
                print(f"{name} -> {url}")


def main():
    """Головна функція програми."""
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
            add_link(url, name)
        elif choice == "2":
            name = input("Введіть коротку назву: ")
            url = get_link(name)
            if url:
                print(f"Початкове посилання: {url}")
        elif choice == "3":
            show_all_links()
        elif choice == "0":
            print("Вихід з програми...")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
