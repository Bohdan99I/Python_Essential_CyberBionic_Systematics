"""Модуль для роботи з температурами у Цельсіях та Фаренгейтах."""


class Temperature:
    """Клас для представлення температури в Цельсіях та Фаренгейтах."""

    def __init__(self, celsius: float = 0.0):
        """
        Ініціалізуємо температуру у градусах Цельсія.

        Args:
            celsius (float): Початкова температура в °C.
        """
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        """Отримуємо температуру у градусах Цельсія."""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        """
        Встановлюємо температуру у градусах Цельсія.

        Args:
            value (float): Значення температури в °C.
        """
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        """Отримуємо температуру у градусах Фаренгейта."""
        return (self._celsius * 9 / 5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        """
        Встановлюємо температуру у градусах Фаренгейта.

        Args:
            value (float): Значення температури в °F.
        """
        self._celsius = (value - 32) * 5 / 9


if __name__ == "__main__":
    temp = Temperature(25)  # 25°C
    print(f"Температура у Цельсіях: {temp.celsius}°C")
    print(f"Температура у Фаренгейтах: {temp.fahrenheit}°F")

    temp.fahrenheit = 212  # встановлюємо 212°F
    print(f"\nНова температура у Цельсіях: {temp.celsius}°C")
    print(f"Нова температура у Фаренгейтах: {temp.fahrenheit}°F")
