"""
Завдання 2.
Вивести зі списку чисел список квадратів парних чисел.
Використати два варіанти: генератор та цикл.
"""


def squares_with_generator(numbers):
    """Повертаємо список квадратів парних чисел за допомогою генератора списку."""
    return [x**2 for x in numbers if x % 2 == 0]


def squares_with_loop(numbers):
    """Повертаємо список квадратів парних чисел за допомогою циклу."""
    result = []
    for x in numbers:
        if x % 2 == 0:
            result.append(x**2)
    return result


def main():
    """Повертаємо список квадратів парних чисел із переданого списку."""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("Оригінальний список:", numbers)

    print("Квадрати парних чисел (генератор):", squares_with_generator(numbers))
    print("Квадрати парних чисел (цикл):", squares_with_loop(numbers))


if __name__ == "__main__":
    main()
