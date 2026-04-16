"""
Модуль містить генератор flatten_list для розгортання вкладених списків.
"""


def flatten_list(nested_list):
    """
    Рекурсивно розгортає вкладений список у плаский.

    Args:
        nested_list (list): список, який може містити інші списки або числа.

    Yields:
        int: елементи у пласкому порядку.
    """
    for element in nested_list:
        if isinstance(element, list):
            yield from flatten_list(element)
        else:
            yield element


if __name__ == "__main__":
    data = [1, [2, [3, 4], 5], 6, [7, [8, [9]]]]
    print(list(flatten_list(data)))
