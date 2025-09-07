"""
Завдання 2.
"""


def calculator():
    """
    Функція-калькулятор.
    Дозволяє виконувати базові операції (+, -, *, /, **).
    При введенні 'exit' програма завершується.
    """
    print("🧮 Калькулятор (введіть 'exit' щоб завершити)")
    print("Операції: +, -, *, /, **")

    while True:
        try:
            expr = input("\nВведіть вираз (наприклад: 2 + 3): ")

            if expr.lower() == "exit":
                print("✅ Програма завершена.")
                break

            parts = expr.split()
            if len(parts) != 3:
                print("❌ Помилка: вираз має бути у форматі 'число операція число'")
                continue

            a, op, b = parts
            a = float(a)
            b = float(b)

            if op == "+":
                result = a + b
            elif op == "-":
                result = a - b
            elif op == "*":
                result = a * b
            elif op == "/":
                if b == 0:
                    raise ZeroDivisionError("Ділення на нуль!")
                result = a / b
            elif op == "**":
                if a == 0 and b < 0:
                    raise ValueError("Не можна зводити 0 у від’ємний степінь!")
                result = a**b
            else:
                print("❌ Помилка: невідома операція")
                continue

            print(f"Результат: {result}")

        except ValueError as e:
            print(f"❌ Помилка значення: {e}")
        except ZeroDivisionError as e:
            print(f"❌ {e}")


if __name__ == "__main__":
    calculator()
