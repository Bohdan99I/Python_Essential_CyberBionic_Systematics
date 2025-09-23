"""Модуль для підрахунку частоти слів у тексті за допомогою регулярних виразів."""

import re
from collections import Counter


def word_frequency(text: str):
    """Повертає частоту слів у рядку text як словник."""
    words = re.findall(r"\w+", text.lower(), flags=re.UNICODE)
    return Counter(words)


def main():
    """Головна функція програми."""
    sample_text = "Python — це мова програмування. Python дуже популярна мова!"
    result = word_frequency(sample_text)

    for word, count in result.items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
