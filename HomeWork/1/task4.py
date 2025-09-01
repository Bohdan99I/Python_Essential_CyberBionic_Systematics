"""Модуль з класами Car та CarShowroom для моделювання автосалону."""


class Car:
    """Клас, що описує автомобіль."""

    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        """Повертає рядкове представлення автомобіля."""
        return f"{self.brand} {self.model} ({self.year}) - ${self.price}"


class CarShowroom:
    """Клас, що описує автосалон з переліком автомобілів."""

    def __init__(self):
        self.cars = []  # список доступних авто

    def add_car(self, car):
        """Додає авто в автосалон."""
        self.cars.append(car)

    def show_cars(self):
        """Виводить список усіх авто."""
        if not self.cars:
            print("В автосалоні немає автомобілів.")
        else:
            print("Автомобілі в автосалоні:")
            for car in self.cars:
                print(car)

    def sell_car(self, brand, model):
        """Продає авто за маркою і моделлю."""
        for car in self.cars:
            if car.brand == brand and car.model == model:
                self.cars.remove(car)
                print(f"Автомобіль {car} продано!")
                return
        print(f"Автомобіль {brand} {model} не знайдено.")


# --- Тестуємо ---
if __name__ == "__main__":
    showroom = CarShowroom()

    # додаємо авто
    car1 = Car("Toyota", "Camry", 2020, 20000)
    car2 = Car("BMW", "X5", 2022, 50000)
    car3 = Car("Audi", "A4", 2021, 30000)

    showroom.add_car(car1)
    showroom.add_car(car2)
    showroom.add_car(car3)

    showroom.show_cars()

    # продаємо авто
    showroom.sell_car("BMW", "X5")

    # список після продажу
    showroom.show_cars()
