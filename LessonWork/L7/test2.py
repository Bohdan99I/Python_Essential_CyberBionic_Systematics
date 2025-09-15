"""
Модуль містить генератор паролів з налаштуваннями.
"""

import string
import random


def password_generator(
    length: int = 8,
    use_upper: bool = True,
    use_digits: bool = True,
    use_special: bool = True,
):
    """
    Генератор випадкових паролів.

    Args:
        length (int, optional): довжина паролю. За замовчуванням 8.
        use_upper (bool, optional): використання великих літер.
        use_digits (bool, optional): використання цифр.
        use_special (bool, optional): використання спецсимволів.

    Yields:
        str: випадковий пароль заданої довжини.
    """
    chars = list(string.ascii_lowercase)

    if use_upper:
        chars.extend(string.ascii_uppercase)
    if use_digits:
        chars.extend(string.digits)
    if use_special:
        chars.extend(string.punctuation)

    if not chars:
        raise ValueError("Не вибрано жодного набору символів для генерації!")

    while True:
        yield "".join(random.choice(chars) for _ in range(length))


if __name__ == "__main__":
    gen = password_generator(
        length=12, use_upper=True, use_digits=True, use_special=True
    )

    # Генеруємо 5 паролів
    for _ in range(5):
        print(next(gen))
