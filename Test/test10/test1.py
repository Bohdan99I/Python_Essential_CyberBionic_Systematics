"""
Відкриємо лог-файл та читаємо його, виводимо тільки дату.
"""

with open("log.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if line:
            date = line.split(" ")[0]
            print(date.lstrip("["))
