"""Модуль для підрахунку кількості повнолітніх людей
в Україні та США за допомогою @classmethod.
"""

from datetime import date


class MyClass1:
    """Базовий клас для опису людини."""

    # Список для збереження всіх створених об'єктів
    _instances = []

    def __init__(self, surname, name, age):
        """Ініціалізація об'єкта людини."""
        self.surname = surname
        self.name = name
        self.age = age
        MyClass1._instances.append(self)

    @classmethod
    def from_birth_year(cls, surname, name, birth_year):
        """Створює об'єкт на основі року народження."""
        return cls(surname, name, date.today().year - birth_year)

    def print_info(self):
        """Виводить інформацію про людину."""
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))

    @classmethod
    def count_adults_ua(cls):
        """Повертає кількість повнолітніх людей в Україні (18+)."""
        return sum(1 for obj in cls._instances if obj.age >= 18)

    @classmethod
    def count_adults_usa(cls):
        """Повертає кількість повнолітніх людей у США (21+)."""
        return sum(1 for obj in cls._instances if obj.age >= 21)


class MyClass2(MyClass1):
    """Похідний клас з додатковою властивістю."""

    color = "White"


m_per1 = MyClass1("Ivanenko", "Ivan", 19)
m_per1.print_info()

m_per2 = MyClass1.from_birth_year("Dovzhenko", "Bogdan", 2000)
m_per2.print_info()

m_per3 = MyClass2.from_birth_year("Sydorchuk", "Petro", 2010)
print(isinstance(m_per3, MyClass2))

m_per4 = MyClass2.from_birth_year("Makuschenko", "Dmytro", 2001)
print(isinstance(m_per4, MyClass1))

print(issubclass(MyClass1, MyClass2))
print(issubclass(MyClass2, MyClass1))

# Використання нових @classmethod
print("Кількість повнолітніх в Україні:", MyClass1.count_adults_ua())
print("Кількість повнолітніх у США:", MyClass1.count_adults_usa())
