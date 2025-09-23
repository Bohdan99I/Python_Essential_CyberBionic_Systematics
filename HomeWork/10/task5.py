"""Модуль для збору даних про учня з послідовних запитів користувача."""

import re


def extract_student_data(
    surname: str, first_name: str, dob: str, email: str, review: str
) -> dict:
    """Формує словник з даних учня."""

    if not re.match(r"\d{2}[./-]\d{2}[./-]\d{4}", dob):
        dob = "Невірний формат дати"

    if not re.match(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email):
        email = "Невірний формат email"

    return {
        "Прізвище": surname.strip() or "Не введено",
        "Ім'я": first_name.strip() or "Не введено",
        "Дата народження": dob,
        "Email": email,
        "Відгук": review.strip() or "Не введено",
    }


def main():
    """Головна функція: поетапний запит даних користувача."""
    print("Будь ласка, введіть дані про учня:")

    surname = input("Прізвище: ")
    first_name = input("Ім'я: ")
    dob = input("Дата народження (дд.мм.рррр): ")
    email = input("Email: ")
    review = input("Відгук про курси: ")

    student_data = extract_student_data(surname, first_name, dob, email, review)

    print("\nВитягнуті дані:")
    for key, value in student_data.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
