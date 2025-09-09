"""
Task 4
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


# --- Створення екземплярів ---
c1 = Contact("Шевченко", "Тарас", 47, "+380671112233", "taras@example.com")
c2 = Contact("Франко", "Іван", 60, "+380501234567", "ivan@example.com")

uc1 = UpdateContact(
    "Леся", "Українка", 42, "+380931234567", "lesya@example.com", "Письменниця"
)
uc2 = UpdateContact(
    "Гоголь", "Микола", 45, "+380671234567", "mykola@example.com", "Прозаїк"
)

# --- Перевірка isinstance ---
print("isinstance перевірки:")
print(isinstance(c1, Contact))  # True
print(isinstance(c1, UpdateContact))  # False
print(isinstance(uc1, Contact))  # True (бо UpdateContact наслідує Contact)
print(isinstance(uc1, UpdateContact))  # True

# --- Перевірка issubclass ---
print("\nissubclass перевірки:")
print(issubclass(UpdateContact, Contact))  # True
print(issubclass(Contact, UpdateContact))  # False
print(issubclass(Contact, object))  # True
