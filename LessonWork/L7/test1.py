"""
Створити функцію генератор яка буде генерувати кожне 7 значення
в заданому з клавіатури діапазоні.
"""


def every_seventh(start_range: int, end_range: int):
    """
    Генератор, що повертає кожне 7 значення в діапазоні [start_range, end_range].

    Args:
        start_range (int): початок діапазону
        end_range (int): кінець діапазону

    Yields:
        int: кожне 7-ме значення з діапазону
    """
    for num in range(start_range, end_range + 1):
        if (num - start_range + 1) % 7 == 0:
            yield num


if __name__ == "__main__":
    user_start = int(input("Введіть початок діапазону: "))
    user_end = int(input("Введіть кінець діапазону: "))

    print("Кожне 7-ме значення у діапазоні:")
    for value in every_seventh(user_start, user_end):
        print(value, end=" ")
