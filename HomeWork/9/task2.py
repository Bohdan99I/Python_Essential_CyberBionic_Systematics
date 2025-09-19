# 📌 МОДУЛІ ТА ПАКЕТИ В PYTHON
# -------------------------------------------------------------
# 🔹 МОДУЛЬ — це файл з кодом Python (.py), який можна імпортувати
# Приклад: example.py
# def add(a, b): return a + b
#
# 🔹 ПАКЕТ — це папка з модулями та файлом __init__.py
# Використовується для групування коду
# -------------------------------------------------------------

# 🔹 СПОСОБИ ІМПОРТУ
# -------------------------------------------------------------
# 1. Стандартний імпорт
import math

print("math.sqrt(16) =", math.sqrt(16))  # 4.0

# 2. Імпорт з перейменуванням
import math as m

print("m.pi =", m.pi)  # 3.1415...

# 3. Імпорт конкретних атрибутів
from math import pi, sqrt

print("pi =", pi)  # 3.1415...
print("sqrt(9) =", sqrt(9))  # 3.0

# 4. Імпорт усіх атрибутів ⚠️ (небажано!)
from math import *

print("sin(0) =", sin(0))  # 0.0

# -------------------------------------------------------------
# 🔹 СТАНДАРТНІ МОДУЛІ
# -------------------------------------------------------------

# ✅ sys – інформація про інтерпретатор
import sys

print("Python version:", sys.version)

# ✅ calendar – робота з календарем
import calendar

print(calendar.month(2025, 9))

# ✅ heapq – черга з пріоритетами (мін-heap)
import heapq

nums = [5, 3, 8, 1]
heapq.heapify(nums)
print("heapified:", nums)

# ✅ bisect – робота з відсортованими списками
import bisect

arr = [1, 3, 4, 7]
bisect.insort(arr, 5)
print("bisect.insort:", arr)

# ✅ array – масиви одного типу
from array import array

a = array("i", [1, 2, 3])
print("array:", a)

# ✅ enum – іменовані константи
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print("Enum example:", Color.RED, Color.RED.value)

# -------------------------------------------------------------
# 🔹 ШЛЯХ ПОШУКУ МОДУЛІВ
# -------------------------------------------------------------
print("sys.path:", sys.path)
