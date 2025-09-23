"""Модуль для аналізу тексту: виведення унікальних слів і статистики."""

import re


def analyze_text(text: str):
    """Аналізує текст і виводить унікальні слова."""
    words = re.findall(r"\w+", text.lower(), flags=re.UNICODE)

    total_words = len(words)
    unique_words = set(words)

    print("Унікальні слова:")
    print(", ".join(sorted(unique_words)))
    print(f"\nЗагальна кількість слів: {total_words}")
    print(f"Кількість унікальних слів: {len(unique_words)}")


def main():
    """Головна функція: запитує текст у користувача та виконує аналіз."""
    user_input = input("Введіть текст: ")
    analyze_text(user_input)


if __name__ == "__main__":
    main()
