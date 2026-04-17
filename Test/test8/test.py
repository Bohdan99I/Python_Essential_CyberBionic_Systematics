"""
Цей скрипт створює файл numbers.txt і записує в нього 10 цілих чисел,
введених користувачем.
"""


def write_numbers():
    """Генерує 10 чисел і записує у файл."""
    numbers = []
    print("Введіть 10 цілих чисел:")

    for i in range(10):
        while True:
            try:
                num = int(input(f"Число {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Будь ласка, введіть коректне ціле число.")

    with open("numbers.txt", "w", encoding="utf-8") as file:
        for num in numbers:
            file.write(f"{num}\n")

    print("Файл numbers.txt успішно створено і заповнено введеними числами.")


if __name__ == "__main__":
    write_numbers()
