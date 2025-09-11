"""
Розширте функціональність класу MyList, додавши:
- метод очищення списку,
- метод додавання елемента у довільне місце,
- метод видалення елемента з кінця,
- метод видалення елемента з довільного місця.
"""


class MyList(object):
    """Клас списку."""

    class _ListNode(object):
        """Внутрішній клас елемента списку."""

        __slots__ = ("value", "prev", "next_node")

        def __init__(self, value, prev=None, next_node=None):
            """Створюємо новий вузол списку."""
            self.value = value
            self.prev = prev
            self.next_node = next_node

        def __repr__(self):
            """Рядкове представлення вузла."""
            return (
                f"MyList._ListNode({self.value}, {id(self.prev)}, {id(self.next_node)})"
            )

    class _Iterator(object):
        """Внутрішній клас ітератора."""

        def __init__(self, list_instance):
            """Створюємо ітератор для об'єкта MyList."""
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            """Повертаємо наступне значення або StopIteration."""
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next_node
            return value

    def __init__(self, iterable=None):
        """Створюємо список MyList."""
        self._length = 0
        self._head = None
        self._tail = None

        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        """Додаємо елемент у кінець списку."""
        node = MyList._ListNode(element)

        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next_node = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def insert(self, index, element):
        """Додаємо елемент у довільне місце."""
        if index < 0 or index > self._length:
            raise IndexError("list index out of range")

        if index == self._length:
            self.append(element)
            return

        current = self._head
        for _ in range(index):
            current = current.next_node

        node = MyList._ListNode(element, prev=current.prev, next_node=current)
        if current.prev:
            current.prev.next_node = node
        else:
            self._head = node
        current.prev = node

        self._length += 1

    def pop(self):
        """Видаляємо елемент з кінця та повертаємо його значення."""
        if self._tail is None:
            raise IndexError("pop from empty list")

        value = self._tail.value
        if self._tail.prev:
            self._tail = self._tail.prev
            self._tail.next_node = None
        else:
            self._head = self._tail = None

        self._length -= 1
        return value

    def remove_at(self, index):
        """Видаляємо елемент за заданим індексом та повертаємо його значення."""
        if not 0 <= index < self._length:
            raise IndexError("list index out of range")

        current = self._head
        for _ in range(index):
            current = current.next_node

        if current.prev:
            current.prev.next_node = current.next_node
        else:
            self._head = current.next_node

        if current.next_node:
            current.next_node.prev = current.prev
        else:
            self._tail = current.prev

        self._length -= 1
        return current.value

    def clear(self):
        """Очищаємо список."""
        self._head = None
        self._tail = None
        self._length = 0

    def __len__(self):
        """Повертаємо довжину списку."""
        return self._length

    def __repr__(self):
        """Рядкове представлення списку."""
        return f"MyList([{', '.join(map(repr, self))}])"

    def __getitem__(self, index):
        """Повертаємо значення за індексом."""
        if not 0 <= index < len(self):
            raise IndexError("list index out of range")

        node = self._head
        for _ in range(index):
            node = node.next_node

        return node.value

    def __iter__(self):
        """Створюємо ітератор для списку."""
        return MyList._Iterator(self)


def main():
    """Демонстрація роботи класу MyList."""
    my_list = MyList([1, 2, 5])
    print("Початковий список:", my_list)

    my_list.insert(1, 100)
    print("Після вставки 100 на позицію 1:", my_list)

    my_list.remove_at(2)
    print("Після видалення елемента на позиції 2:", my_list)

    my_list.pop()
    print("Після видалення останнього елемента:", my_list)

    my_list.clear()
    print("Після очищення:", my_list)


if __name__ == "__main__":
    main()
