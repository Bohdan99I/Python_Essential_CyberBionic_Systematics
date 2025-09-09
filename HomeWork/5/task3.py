"""Модуль для демонстрації роботи hasattr(), getattr(), setattr(), delattr()."""


class Contact:
    """Базовий клас контакту з полями:
    surname, name, age, mob_phone, email.
    """

    def __init__(
        self, surname: str, name: str, age: int, mob_phone: str, email: str
    ) -> None:
        """Ініціалізація атрибутів контакту."""
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email


class UpdateContact(Contact):
    """Клас-нащадок Contact, що додає поле job."""

    def __init__(
        self, surname: str, name: str, age: int, mob_phone: str, email: str, job: str
    ) -> None:
        """Ініціалізація атрибутів, включно з job."""
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job


if __name__ == "__main__":
    c1 = Contact("Шевченко", "Тарас", 35, "+380501112233", "taras@example.com")
    c2 = UpdateContact(
        "Франко", "Іван", 40, "+380631112233", "ivan@example.com", "Письменник"
    )

    print("\n--- Перевірка атрибутів ---")

    # hasattr() → чи існує атрибут
    print("Чи є атрибут 'email' у c1?", hasattr(c1, "email"))
    print("Чи є атрибут 'job' у c1?", hasattr(c1, "job"))

    # getattr() → отримання значення атрибута
    print("Значення 'surname' у c1:", getattr(c1, "surname"))
    # якщо атрибута немає, можна задати значення за замовчуванням
    print("Значення 'job' у c1 (за замовчуванням):", getattr(c1, "job", "Немає роботи"))

    # setattr() → зміна або створення атрибута
    setattr(c1, "email", "new_email@example.com")
    print("Новий email у c1:", c1.email)
    # створимо новий атрибут
    setattr(c1, "nickname", "Kobzar")
    print("Новий атрибут nickname у c1:", c1.nickname)  # pylint: disable=no-member

    # delattr() → видалення атрибута
    delattr(c1, "nickname")
    print("Після видалення nickname:", hasattr(c1, "nickname"))

    print("\n--- Для c2 ---")
    print("Робота (job) у c2:", getattr(c2, "job"))
    setattr(c2, "job", "Політик")
    print("Змінено job у c2:", c2.job)
    delattr(c2, "job")
    print("Атрибут job існує після видалення?", hasattr(c2, "job"))
