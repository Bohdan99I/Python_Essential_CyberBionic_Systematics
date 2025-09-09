"""
Task 6
Виведення усіх методів класів Contact та UpdateContact.
"""


class Contact:
    """Клас для зберігання контактної інформації."""

    def __init__(self, surname, name, age, mob_phone, email):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        """Вивести контактну інформацію."""
        return f"{self.name} {self.surname}, {self.age} років, тел: {self.mob_phone}, email: {self.email}"

    def send_message(self, message):
        """Надіслати повідомлення."""
        return f"Повідомлення '{message}' надіслано на {self.mob_phone}"


class UpdateContact(Contact):
    """Клас-нащадок Contact з додатковим полем job."""

    def __init__(self, surname, name, age, mob_phone, email, job):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self):
        """Вивести інформацію про роботу."""
        return f"{self.name} {self.surname} працює як {self.job}"


# --- Функція для отримання лише методів ---
def get_methods(cls):
    """Повертає список методів класу без службових __методів__."""
    return [
        func
        for func in dir(cls)
        if callable(getattr(cls, func)) and not func.startswith("__")
    ]


print("Методи класу Contact:", get_methods(Contact))
print("Методи класу UpdateContact:", get_methods(UpdateContact))
