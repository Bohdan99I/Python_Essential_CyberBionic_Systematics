"""
Завдання 1.
"""


class Car:
    """
    Клас, який моделює автомобіль.

    Атрибути:
        brand (str): марка автомобіля.
        model (str): модель автомобіля.
        year (int): рік випуску.
        __mileage (int): пробіг (приватний атрибут).
        __engine_status (bool): стан двигуна (приватний атрибут).
    """

    def __init__(self, brand, model, year, mileage):
        """
        Ініціалізує новий автомобіль.

        Args:
            brand (str): марка автомобіля.
            model (str): модель автомобіля.
            year (int): рік випуску.
            mileage (int): початковий пробіг.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.__mileage = mileage
        self.__engine_status = False

    def get_mileage(self):
        """
        Повертає пробіг автомобіля.

        Returns:
            int: поточний пробіг.
        """
        return self.__mileage

    def set_mileage(self, mileage):
        """
        Встановлює новий пробіг автомобіля, якщо він не менший за поточний.

        Args:
            mileage (int): нове значення пробігу.
        """
        if mileage >= self.__mileage:
            self.__mileage = mileage
        else:
            print("Помилка: пробіг не може зменшуватись!")

    def get_engine_status(self):
        """
        Повертає стан двигуна.

        Returns:
            bool: True – увімкнений, False – вимкнений.
        """
        return self.__engine_status

    def set_engine_status(self, status):
        """
        Встановлює стан двигуна.

        Args:
            status (bool): True для увімкнення, False для вимкнення.
        """
        if isinstance(status, bool):
            self.__engine_status = status
        else:
            print("Помилка: стан двигуна повинен бути True або False")

    def display_info(self):
        """
        Виводить інформацію про автомобіль у консоль.
        """
        print(f"Автомобіль: {self.brand} {self.model}, {self.year} р.")
        print(f"Пробіг: {self.__mileage} км")
        print(f"Двигун увімкнено: {self.__engine_status}")


# Приклад використання
if __name__ == "__main__":
    car1 = Car("Toyota", "Camry", 2020, 15000)
    car1.display_info()

    print("\nОновлення пробігу...")
    car1.set_mileage(20000)
    print("Новий пробіг:", car1.get_mileage())

    print("\nСпроба зменшити пробіг...")
    car1.set_mileage(10000)

    print("\nУвімкнення двигуна...")
    car1.set_engine_status(True)
    print("Стан двигуна:", car1.get_engine_status())

    car1.display_info()
