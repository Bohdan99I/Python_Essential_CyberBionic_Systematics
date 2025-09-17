"""Скрипт для генерації 10000 випадкових чисел і обчислення їх суми з файлу"""

import random


def generate_numbers():
    """Генерує 10000 випадкових чисел і записує у файл."""
    with open("numbers.txt", "w", encoding="utf-8") as file:
        for _ in range(10000):
            file.write(f"{random.uniform(0, 1000)}\n")


def sum_numbers():
    """Зчитує числа з файлу та обчислює їхню суму."""
    total = 0
    with open("numbers.txt", "r", encoding="utf-8") as file:
        for line in file:
            total += float(line.strip())
    print(f"Сума чисел: {total}")


if __name__ == "__main__":
    generate_numbers()
    print("Файл numbers.txt успішно створено!")
    sum_numbers()
