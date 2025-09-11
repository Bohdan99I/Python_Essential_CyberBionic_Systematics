"""
Реалізуйте цикл, який перебиратиме всі значення ітерабельного об'єкту iterable.
"""

# -------------------------------
# Варіант 1 цикл for
iterable = [10, 20, 30, 40, 50]

print("Перебір за допомогою for:")
for element in iterable:
    print(element)

# -------------------------------
# Варіант 2 через iter() та next()
iterable = [10, 20, 30, 40, 50]
iterator = iter(iterable)

print("\nПеребір за допомогою iter() та next():")
while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break

# -------------------------------
# Варіант 3 через while
iterable = [10, 20, 30, 40, 50]
iterator = iter(iterable)

print("\nПеребір за допомогою while:")
while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break
