"""Ієрархія класів транспортних засобів."""


class Vehicle:
    """Базовий клас для всіх транспортних засобів."""

    def __init__(self, make: str, model: str, year: int):
        """
        Ініціалізує транспортний засіб.

        Args:
            make (str): виробник
            model (str): модель
            year (int): рік випуску
        """
        self.make = make
        self.model = model
        self.year = year

    def info(self):
        """Вивести загальну інформацію про транспортний засіб."""
        print(f"{self.year} {self.make} {self.model}")


class Car(Vehicle):
    """Легковий автомобіль."""

    def __init__(self, make: str, model: str, year: int, doors: int):
        """
        Ініціалізує автомобіль.

        Args:
            doors (int): кількість дверей
        """
        super().__init__(make, model, year)
        self.doors = doors

    def info(self):
        """Вивести інформацію про автомобіль."""
        super().info()
        print(f"Дверей: {self.doors}")


class Motorcycle(Vehicle):
    """Мотоцикл."""

    def __init__(self, make: str, model: str, year: int, engine_cc: int):
        """
        Ініціалізує мотоцикл.

        Args:
            engine_cc (int): об'єм двигуна у куб. см
        """
        super().__init__(make, model, year)
        self.engine_cc = engine_cc

    def info(self):
        """Вивести інформацію про мотоцикл."""
        super().info()
        print(f"Об'єм двигуна: {self.engine_cc} см³")


class Truck(Vehicle):
    """Вантажівка."""

    def __init__(self, make: str, model: str, year: int, capacity_t: float):
        """
        Ініціалізує вантажівку.

        Args:
            capacity_t (float): вантажопідйомність у тоннах
        """
        super().__init__(make, model, year)
        self.capacity_t = capacity_t

    def info(self):
        """Вивести інформацію про вантажівку."""
        super().info()
        print(f"Вантажопідйомність: {self.capacity_t} тонн")


def main():
    """Основна логіка програми."""
    car1 = Car("Toyota", "Camry", 2022, 4)
    moto1 = Motorcycle("Yamaha", "MT-07", 2021, 689)
    truck1 = Truck("Volvo", "FH16", 2020, 25)

    vehicles = [car1, moto1, truck1]

    for vehicle in vehicles:
        vehicle.info()
        print("-" * 30)


if __name__ == "__main__":
    main()
