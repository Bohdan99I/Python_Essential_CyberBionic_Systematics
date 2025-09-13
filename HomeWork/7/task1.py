"""
Завдання 1.
Генератор, який повертає елементи списку у зворотному порядку (аналог reversed).
"""


def reverse_generator(data):
    """Генератор, що повертає елементи списку у зворотному порядку."""
    for i in range(len(data) - 1, -1, -1):
        yield data[i]


def main():
    """Демонстрація роботи генератора reverse_generator."""
    my_list = [1, 2, 3, 4, 5]
    print("Оригінальний список:", my_list)

    print("Список у зворотному порядку:")
    for item in reverse_generator(my_list):
        print(item, end=" ")
    print()


if __name__ == "__main__":
    main()
