"""
Модуль для роботи з файлами:
"""

import datetime

LOG_FILE = "log.txt"
FILENAME = "numbers.txt"


def log_action(action: str) -> None:
    """Записую дію у лог-файл."""
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] {action}\n")


def open_file(file_name: str, mode: str):
    """Відкриваю файл і логую дію."""
    log_action(f"Відкрито файл '{file_name}' у режимі '{mode}'")
    return open(file_name, mode, encoding="utf-8")


def write_file(file, data: str) -> None:
    """Записую дані у файл і логую дію."""
    file.write(data + "\n")
    log_action(f"Записано у файл: {data}")


def read_file(file) -> str:
    """Читаю вміст файлу і логую дію."""
    content = file.read()
    log_action("Прочитано вміст файлу")
    return content


def close_file(file, file_name: str) -> None:
    """Закриваю файл і логую дію."""
    file.close()
    log_action(f"Файл '{file_name}' закрито")


def read_log() -> str:
    """Зчитую лог-файл і повертаю його вміст."""
    with open(LOG_FILE, "r", encoding="utf-8") as log:
        return log.read()


if __name__ == "__main__":
    f = open_file(FILENAME, "w")
    write_file(f, "123")
    write_file(f, "456")
    close_file(f, FILENAME)

    f = open_file(FILENAME, "r")
    content = read_file(f)
    print("Вміст файлу:\n", content)
    close_file(f, FILENAME)

    print("\nЛог дій:")
    print(read_log())
