"""Модуль для вилучення дат народження, телефонів та email з тексту у файлі."""

import re


def extract_data_from_file(input_file: str, output_file: str):
    """Зчитує текст із input_file, знаходить усі дати народження, телефони і email,
    та записує їх у output_file."""

    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    date_pattern = r"\b\d{2}[./-]\d{2}[./-]\d{4}\b"
    phone_pattern = r"\+?\d[\d\s()-]{7,}\d"
    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    dates = re.findall(date_pattern, content)
    phones = re.findall(phone_pattern, content)
    emails = re.findall(email_pattern, content)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("Знайдені дати народження:\n")
        file.write("\n".join(dates) if dates else "Не знайдено")
        file.write("\n\n")

        file.write("Знайдені телефони:\n")
        file.write("\n".join(phones) if phones else "Не знайдено")
        file.write("\n\n")

        file.write("Знайдені email:\n")
        file.write("\n".join(emails) if emails else "Не знайдено")


def main():
    """Головна функція: тестує вилучення кількох даних з файлу."""
    extract_data_from_file("input.txt", "output.txt")
    print("Дані збережено у output.txt")


if __name__ == "__main__":
    main()
