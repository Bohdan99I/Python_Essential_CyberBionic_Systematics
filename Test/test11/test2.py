"""
Цей модуль імітує роботу радіоприймача.
"""


class Radio:
    """
    Клас Radio.
    """

    def __init__(self, current_channel=99.5, volume=5):
        """Об'єкт Radio."""
        self.is_on = False
        self.current_channel = current_channel
        self.volume = volume

    def toggle_power(self):
        """Увімкнення/вимкнення радіо."""
        self.is_on = not self.is_on
        if self.is_on:
            print("Радіо увімкнено.")
        else:
            print("Радіо вимкнено.")

    def set_volume(self, new_volume):
        """Гучність."""
        if self.is_on:
            try:
                vol = int(new_volume)
                if 0 <= vol <= 10:
                    self.volume = vol
                    print(f"Гучність встановлено на {self.volume}.")
                else:
                    print("Помилка: Гучність має бути в діапазоні від 0 до 10.")
            except ValueError:
                print("Помилка: Введіть числове значення для гучності.")
        else:
            print("Спершу увімкніть радіо.")

    def change_channel(self, new_channel):
        """Перемикає канал."""
        if self.is_on:
            try:
                chan = float(new_channel)
                self.current_channel = chan
                print(f"Переключено на канал {self.current_channel} МГц.")
            except ValueError:
                print("Помилка: Введіть числове значення для каналу.")
        else:
            print("Спершу увімкніть радіо.")

    def get_status(self):
        """Показує поточний стан радіо."""
        if self.is_on:
            print(
                f"Статус: Увімкнено. Канал: {self.current_channel} МГц. Гучність: {self.volume}."
            )
        else:
            print("Статус: Вимкнено.")


def main():
    """Основна функція для запуску інтерактивного радіо."""
    my_radio = Radio()
    print("Вітаємо в симуляторі радіоприймача!")
    print(
        "Доступні команди: 'включити', 'виключити', 'гучність', 'канал', 'статус', 'вихід'."
    )

    while True:
        command = input("\nВведіть команду: ").strip().lower().split()

        if not command:
            continue

        action = command[0]
        arg = command[1] if len(command) > 1 else None

        if action == "вихід":
            print("До побачення!")
            break
        elif action == "включити":
            if not my_radio.is_on:
                my_radio.toggle_power()
            else:
                print("Радіо вже увімкнено.")
        elif action == "виключити":
            if my_radio.is_on:
                my_radio.toggle_power()
            else:
                print("Радіо вже вимкнено.")
        elif action == "гучність" and arg:
            my_radio.set_volume(arg)
        elif action == "канал" and arg:
            my_radio.change_channel(arg)
        elif action == "статус":
            my_radio.get_status()
        else:
            print("Невідома команда або відсутній параметр. Спробуйте ще.")


if __name__ == "__main__":
    main()
    