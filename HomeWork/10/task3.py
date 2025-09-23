"""Модуль для виведення останніх трьох символів кожного слова з пропозиції користувача."""

import re


def last_three_chars(sentence: str):
    """Друкує останні три символи кожного слова в рядку sentence."""
    words = re.findall(r"\w+", sentence, flags=re.UNICODE)

    for word in words:
        print(word[-3:] if len(word) >= 3 else word)


def main():
    """Головна функція програми."""
    user_input = input("Введіть пропозицію: ")
    last_three_chars(user_input)


if __name__ == "__main__":
    main()
