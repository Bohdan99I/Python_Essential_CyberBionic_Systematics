"""
Ітератор, який повертає елементи списку у зворотному порядку.
"""


class ReverseIterator:
    """Ітератор для проходження списку у зворотному порядку."""

    def __init__(self, data):
        """Ініціалізація ітератора зі списком data."""
        self._data = data
        self._index = len(data) - 1

    def __iter__(self):
        """Повертаємо ітератор."""
        return self

    def __next__(self):
        """Повертаємо наступний елемент у зворотному порядку."""
        if self._index < 0:
            raise StopIteration
        value = self._data[self._index]
        self._index -= 1
        return value


def main():
    """Демонстрація роботи ReverseIterator: проходження списку у зворотному порядку."""
    my_list = [1, 2, 3, 4, 5]
    print("Оригінальний список:", my_list)

    print("Список у зворотному порядку:")
    for item in ReverseIterator(my_list):
        print(item, end=" ")
    print()


if __name__ == "__main__":
    main()
