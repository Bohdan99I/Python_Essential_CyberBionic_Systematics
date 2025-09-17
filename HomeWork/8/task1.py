"""Скрипт для генерації 10000 випадкових чисел і обчислення їх суми з файлу"""

import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def generate_numbers():
    """Генерує 10000 випадкових чисел і записує у файл."""
    file_path = os.path.join(BASE_DIR, "numbers.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        for _ in range(10000):
            file.write(f"{random.uniform(0, 1000)}\n")


def sum_numbers():
    """Зчитує числа з файлу та обчислює їхню суму."""
    total = 0
    file_path = os.path.join(BASE_DIR, "numbers.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            total += float(line.strip())
    print(f"Сума чисел: {total}")


if __name__ == "__main__":
    generate_numbers()
    print("Файл numbers.txt успішно створено!")
    sum_numbers()
