"""
Завдання 4.
"""


class ForbiddenValueError(Exception):
    """Користувацький виняток для забороненого значення."""


def check_value(user_input: str) -> None:
    """
    Перевіряє введене значення і викидає виняток,
    якщо воно дорівнює 'error'.

    :param user_input: рядок, введений користувачем
    :raises ForbiddenValueError: якщо введене значення заборонене
    """
    if user_input.lower() == "error":
        raise ForbiddenValueError("❌ Заборонене значення 'error'!")
    print(f"✅ Ви ввели: {user_input}")


def main():
    """Головна функція програми."""
    try:
        value = input("Введіть будь-яке значення: ")
        check_value(value)
    except ForbiddenValueError as e:
        print(f"⚠️ Виникла помилка: {e}")


if __name__ == "__main__":
    main()
