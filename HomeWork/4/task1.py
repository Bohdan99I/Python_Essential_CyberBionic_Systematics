# 📌 Завдання 1: Основні стандартні винятки в Python

# -------------------------------------------------
# Обробка винятків
# ✅ Використовуємо конструкцію try-except-else-finally

try:
    x = 10 / 2
except ZeroDivisionError:
    print("Помилка: ділення на нуль!")
else:
    print("Результат:", x)
finally:
    print("Блок finally виконується завжди")


# -------------------------------------------------
# Створення власного винятку
class MyCustomError(Exception):
    """Користувацький виняток."""

    pass


def risky_function(value):
    if value == 13:
        raise MyCustomError("Значення 13 заборонене!")
    return value * 2


try:
    print(risky_function(13))
except MyCustomError as e:
    print("Перехоплено:", e)


# -------------------------------------------------
# Приклади стандартних винятків

# ArithmeticError → ZeroDivisionError
try:
    1 / 0
except ZeroDivisionError:
    print("❌ ZeroDivisionError: ділення на нуль")

# AttributeError
try:
    [].fake_method()
except AttributeError:
    print("❌ AttributeError: метод не існує")

# IndexError
try:
    [1, 2, 3][5]
except IndexError:
    print("❌ IndexError: неправильний індекс")

# KeyError
try:
    {"a": 1}["b"]
except KeyError:
    print("❌ KeyError: ключ відсутній")

# NameError
try:
    print(unknown_var)
except NameError:
    print("❌ NameError: змінна не визначена")

# TypeError
try:
    "abc" + 123
except TypeError:
    print("❌ TypeError: несумісні типи")

# ValueError
try:
    int("not_a_number")
except ValueError:
    print("❌ ValueError: неправильне значення")

# ImportError
try:
    import not_existing_module
except ImportError:
    print("❌ ImportError: модуль не знайдено")

# MemoryError (симуляція, реально викликати небезпечно)
# raise MemoryError("Недостатньо пам’яті")


# -------------------------------------------------
# Попередження
import warnings

warnings.warn("Це приклад попередження", UserWarning)
