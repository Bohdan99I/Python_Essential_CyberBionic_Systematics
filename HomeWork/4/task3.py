"""
Завдання 3.
"""


class InvalidEmployeeDataError(Exception):
    """Користувацький виняток для некоректних даних співробітника."""


class Employee:
    """Клас, що описує співробітника."""

    def __init__(
        self, first_name: str, last_name: str, department: str, start_year: int
    ):
        """
        Ініціалізація співробітника.

        :param first_name: Ім’я
        :param last_name: Прізвище
        :param department: Відділ
        :param start_year: Рік початку роботи
        :raises InvalidEmployeeDataError: Якщо дані некоректні
        """
        if not first_name.isalpha() or not last_name.isalpha():
            raise InvalidEmployeeDataError(
                "Ім’я та прізвище мають містити тільки літери."
            )
        if not department:
            raise InvalidEmployeeDataError("Відділ не може бути порожнім.")
        if not 1900 <= start_year <= 2100:
            raise InvalidEmployeeDataError("Некоректний рік початку роботи.")

        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.start_year = start_year

    def __str__(self):
        """Рядкове представлення співробітника."""
        return (
            f"{self.first_name} {self.last_name}, "
            f"відділ: {self.department}, рік початку: {self.start_year}"
        )


def main():
    """Головна функція програми."""
    employees = []

    try:
        n = int(input("Скільки співробітників ви хочете ввести? "))
    except ValueError:
        print("❌ Некоректне число.")
        return

    for i in range(n):
        print(f"\nВведення даних для співробітника {i + 1}:")
        try:
            first_name = input("Ім’я: ")
            last_name = input("Прізвище: ")
            department = input("Відділ: ")
            start_year = int(input("Рік початку роботи: "))

            employee = Employee(first_name, last_name, department, start_year)
            employees.append(employee)

        except (ValueError, InvalidEmployeeDataError) as e:
            print(f"❌ Помилка: {e}")
            continue

    try:
        year = int(input("\nВведіть рік для пошуку співробітників: "))
    except ValueError:
        print("❌ Некоректний рік.")
        return

    print(f"\n✅ Співробітники, прийняті після {year}:")
    found = False
    for emp in employees:
        if emp.start_year > year:
            print(emp)
            found = True

    if not found:
        print("Немає співробітників, що задовольняють умову.")


if __name__ == "__main__":
    main()
