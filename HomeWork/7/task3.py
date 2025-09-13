"""
Модуль для генерації n перших простих чисел за допомогою функції-генератора.
"""


def prime_numbers(n):
    """
    Генератор, що повертає n перших простих чисел.
    """
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1


def is_prime(number):
    """
    Перевіряємо, чи є число простим.
    """
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


for p in prime_numbers(10):
    print(p, end=" ")
