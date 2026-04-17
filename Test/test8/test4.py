"""
Модуль для роботи з файлами: відкриття, читання, запис та логування дій у файл.
"""

import os
from datetime import datetime


def log_action(log_file, action):
    """Записує дію у лог-файл."""
    with open(log_file, "a", encoding="utf-8") as log:
        log.write(f"{datetime.now()} - {action}\n")


def open_file(filename, mode):
    """Відкриває файл і логую дію."""
    log_file = f"{os.path.splitext(filename)[0]}_log.txt"
    file = open(filename, mode, encoding="utf-8")
    log_action(log_file, f"Відкрито файл '{filename}' у режимі '{mode}'")
    return file, log_file


def write_file(filename, data):
    """Записує дані у файл і логую дію."""
    file, log_file = open_file(filename, "w")
    file.write(data)
    log_action(log_file, f"Записано дані у файл '{filename}'")
    file.close()
    log_action(log_file, f"Файл '{filename}' закрито")


def read_file(filename):
    """Читає вміст файлу і логую дію."""
    file, log_file = open_file(filename, "r")
    content = file.read()
    log_action(log_file, f"Прочитано файл '{filename}'")
    file.close()
    log_action(log_file, f"Файл '{filename}' закрито")
    return content


write_file("numbers2.txt", "10 20 30")
print(read_file("numbers2.txt"))
