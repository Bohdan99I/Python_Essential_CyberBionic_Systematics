# 📌 Інтроспекція та Рефлексія в Python

# -------------------------------------------------
# 🔍 Інтроспекція
# ✅ Дозволяє отримати інформацію про об'єкт під час виконання

# ✅ правильно
x = 42
print(type(x))  # <class 'int'>
print(dir(x))  # перелік атрибутів і методів
print(x.__class__)  # <class 'int'>

# ❌ неправильно
# Спроба вгадати тип "на око", без використання вбудованих інструментів


# -------------------------------------------------
# 🪞 Рефлексія
# ✅ Дозволяє змінювати структуру або поведінку об'єкта під час виконання


class User:
    def __init__(self, name):
        self.name = name


user = User("Ivan")

# ✅ правильно
setattr(user, "age", 25)  # додаємо новий атрибут
print(getattr(user, "age"))  # 25

# ❌ неправильно
# user.age   # виклик неіснуючого атрибуту → AttributeError


# -------------------------------------------------
# ⚠️ Exception при роботі з атрибутами

try:
    print(getattr(user, "email"))
except AttributeError:
    print("Атрибут не знайдено!")  # Обробка виключення


# -------------------------------------------------
# 📖 Важливі функції та атрибути для інтроспекції
# - type(), dir(), __class__, __dict__
# - isinstance(), issubclass()
# - hasattr(), getattr(), setattr(), delattr()
# - модуль inspect


# -------------------------------------------------
# 📖 Приклад коду з інтроспекцією та рефлексією

import inspect


class Car:
    """Простий клас для прикладу"""

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


car = Car("Tesla", 2022)

# Інтроспекція
print(type(car))  # <class '__main__.Car'>
print(car.__dict__)  # {'brand': 'Tesla', 'year': 2022}
print(inspect.getmembers(car))  # усі атрибути та методи

# Рефлексія
setattr(car, "color", "red")  # додаємо нову властивість
print(car.color)  # red
