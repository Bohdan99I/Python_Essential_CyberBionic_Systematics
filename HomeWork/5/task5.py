"""
Task 5
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
uc1 = UpdateContact(
    "Леся", "Українка", 42, "+380931234567", "lesya@example.com", "Письменниця"
)

print("=== Стан класів та об'єктів ДО видалення атрибуту job ===")
print("Атрибути класу Contact:", Contact.__dict__)
print("Атрибути екземпляра c1:", c1.__dict__)
print("Атрибути класу UpdateContact:", UpdateContact.__dict__)
print("Атрибути екземпляра uc1:", uc1.__dict__)

# --- Видалення атрибуту job ---
delattr(uc1, "job")

print("\n=== Стан класів та об'єктів ПІСЛЯ видалення атрибуту job ===")
print("Атрибути класу Contact:", Contact.__dict__)
print("Атрибути екземпляра c1:", c1.__dict__)
print("Атрибути класу UpdateContact:", UpdateContact.__dict__)
print("Атрибути екземпляра uc1:", uc1.__dict__)

# --- Висновок ---
print("\nВисновок:")
print("Атрибут job належав екземпляру uc1, а не самому класу UpdateContact.")
print(
    "Після видалення атрибуту job у конкретного об'єкта uc1,"
    " клас UpdateContact все ще зберігає методи, що працюють з job."
)
print(
    "Але спроба виклику uc1.get_message() тепер викличе помилку AttributeError, бо job у нього більше немає."
)
