"""Модуль з реалізацією класів Contact та UpdateContact."""


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

    def get_contact(self) -> str:
        """Повертає повну інформацію про контакт."""
        return (
            f"Прізвище: {self.surname}, Ім'я: {self.name}, "
            f"Вік: {self.age}, Телефон: {self.mob_phone}, "
            f"Email: {self.email}"
        )

    def send_message(self, text: str) -> None:
        """Надсилає повідомлення на мобільний телефон."""
        print(f"Надіслано повідомлення '{text}' на {self.mob_phone}")


class UpdateContact(Contact):
    """Клас-нащадок Contact, що додає поле job."""

    def __init__(
        self, surname: str, name: str, age: int, mob_phone: str, email: str, job: str
    ) -> None:
        """Ініціалізація атрибутів, включно з job."""
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self) -> str:
        """Повертає інформацію про контакт разом із роботою."""
        return (
            f"Контакт: {self.name} {self.surname}, "
            f"Робота: {self.job}, Email: {self.email}"
        )


if __name__ == "__main__":
    c1 = Contact("Шевченко", "Тарас", 35, "+380501112233", "taras@example.com")
    c2 = UpdateContact(
        "Франко", "Іван", 40, "+380631112233", "ivan@example.com", "Письменник"
    )

    print(c1.get_contact())
    c1.send_message("Привіт!")

    print(c2.get_contact())
    print(c2.get_message())
    c2.send_message("Як справи?")

    print("\n--- Атрибути класів ---")
    print("c1.__dict__:", c1.__dict__)
    print("c2.__dict__:", c2.__dict__)

    print("\n--- Базові класи ---")
    print("Contact.__base__:", Contact.__base__)
    print("UpdateContact.__base__:", UpdateContact.__base__)
    print("Contact.__bases__:", Contact.__bases__)
    print("UpdateContact.__bases__:", UpdateContact.__bases__)
