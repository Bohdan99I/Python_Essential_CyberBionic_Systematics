"""Модуль для роботи з класами людей та перевірки повноліття
в Україні та США за допомогою статичних методів.
"""

from datetime import date


class MyClass1:
    """Базовий клас для опису людини."""

    def __init__(self, surname, name, age):
        """Ініціалізація об'єкта людини."""
        self.surname = surname
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, surname, name, birth_year):
        """Створює об'єкт на основі року народження."""
        return cls(surname, name, date.today().year - birth_year)

    def print_info(self):
        """Виводить інформацію про людину."""
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))

    @staticmethod
    def is_adult_ua(age):
        """Перевіряє повноліття в Україні (18 років)."""
        return age >= 18

    @staticmethod
    def is_adult_usa(age):
        """Перевіряє повноліття в США (21 рік)."""
        return age >= 21


class MyClass2(MyClass1):
    """Похідний клас з додатковою властивістю."""

    color = "White"


m_per1 = MyClass1("Ivanenko", "Ivan", 19)
m_per1.print_info()
print("Повноліття в Україні:", MyClass1.is_adult_ua(m_per1.age))
print("Повноліття в США:", MyClass1.is_adult_usa(m_per1.age))

m_per2 = MyClass1.from_birth_year("Dovzhenko", "Bogdan", 2000)
m_per2.print_info()
print("Повноліття в Україні:", MyClass1.is_adult_ua(m_per2.age))
print("Повноліття в США:", MyClass1.is_adult_usa(m_per2.age))

m_per3 = MyClass2.from_birth_year("Sydorchuk", "Petro", 2010)
print(isinstance(m_per3, MyClass2))

m_per4 = MyClass2.from_birth_year("Makuschenko", "Dmytro", 2001)
print(isinstance(m_per4, MyClass1))

print(issubclass(MyClass1, MyClass2))
print(issubclass(MyClass2, MyClass1))
