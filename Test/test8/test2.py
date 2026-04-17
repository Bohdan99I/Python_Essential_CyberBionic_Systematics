"""
Цей скрипт читає числа з файлу numbers.txt і виводить їхню суму.
"""


def read_and_sum():
    """Зчитує числа з файлу та обчислює їхню суму."""
    with open("numbers.txt", "r", encoding="utf-8") as file:
        numbers = [int(line.strip()) for line in file]
    total = sum(numbers)
    print("Сума чисел у файлі:", total)


if __name__ == "__main__":
    read_and_sum()
