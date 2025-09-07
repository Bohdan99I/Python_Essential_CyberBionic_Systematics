"""
Програма спортивного комплексу з меню
"""


class CoachNotFoundError(Exception):
    """Користувацький виняток для випадку, коли тренер не знайдений."""


# Дані спортивного комплексу
sports = {1: "Футбол", 2: "Баскетбол", 3: "Плавання", 4: "Теніс", 5: "Йога"}

coaches = {
    "Іванов": "Футбол",
    "Петренко": "Баскетбол",
    "Сидоренко": "Плавання",
    "Коваль": "Теніс",
    "Шевченко": "Йога",
}

schedule = {
    "Футбол": "Пн, Ср, Пт 18:00-20:00",
    "Баскетбол": "Вт, Чт 17:00-19:00",
    "Плавання": "Пн, Ср, Пт 07:00-09:00",
    "Теніс": "Сб, Нд 10:00-12:00",
    "Йога": "Вт, Чт 18:00-19:30",
}

price = {"Футбол": 150, "Баскетбол": 130, "Плавання": 200, "Теніс": 180, "Йога": 100}


def show_sports():
    """Виводить перелік видів спорту."""
    print("Види спорту:")
    for num, sport in sports.items():
        print(f"{num}. {sport}")


def show_coaches():
    """Виводить команду тренерів."""
    print("Команда тренерів:")
    for name, sport in coaches.items():
        print(f"{name} - {sport}")


def show_schedule():
    """Виводить розклад тренувань."""
    print("Розклад тренувань:")
    for sport, time in schedule.items():
        print(f"{sport}: {time}")


def show_prices():
    """Виводить вартість тренувань."""
    print("Вартість тренувань (грн):")
    for sport, cost in price.items():
        print(f"{sport}: {cost}")


def find_coach():
    """Шукає тренера за прізвищем та викликає виняток, якщо не знайдено."""
    last_name = input("Введіть прізвище тренера для пошуку: ")
    if last_name in coaches:
        print(f"{last_name} веде {coaches[last_name]}")
    else:
        raise CoachNotFoundError(f"Тренер з прізвищем '{last_name}' не знайдений.")


def main():
    """Головне меню програми."""
    while True:
        print("\nМеню спортивного комплексу:")
        print("1 - Перелік видів спорту")
        print("2 - Команда тренерів")
        print("3 - Розклад тренувань")
        print("4 - Вартість тренування")
        print("5 - Пошук тренера")
        print("0 - Вихід")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            show_sports()
        elif choice == "2":
            show_coaches()
        elif choice == "3":
            show_schedule()
        elif choice == "4":
            show_prices()
        elif choice == "5":
            try:
                find_coach()
            except CoachNotFoundError as e:
                print(f"⚠️ {e}")
        elif choice == "0":
            print("Дякуємо за користування програмою!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
