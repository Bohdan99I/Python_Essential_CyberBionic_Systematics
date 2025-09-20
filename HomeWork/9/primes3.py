"""Модуль для роботи з простими числами."""


def is_prime(n):
    """Перевіряє, чи є число простим"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_primes(limit):
    """Генерує всі прості числа до limit (виключно)"""
    return [x for x in range(2, limit) if is_prime(x)]
