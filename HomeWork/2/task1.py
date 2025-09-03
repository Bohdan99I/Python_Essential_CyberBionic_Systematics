"""Програма для роботи з редактором документів (Editor / ProEditor)."""


class Editor:
    """Базовий редактор з обмеженими можливостями."""

    def view_document(self):
        """Відкрити документ для перегляду."""
        print("Документ відкрито для перегляду.")

    def edit_document(self):
        """Редагування доступне тільки у Pro версії."""
        print("Редагування документів недоступне у безкоштовній версії.")


class ProEditor(Editor):
    """Редактор з повними можливостями."""

    def edit_document(self):
        """Відкрити документ для редагування."""
        print("Документ відкрито для редагування.")


def main():
    """Основна логіка програми."""
    license_key = "12345"  # правильний ключ

    # Безкоштовна версія
    editor = Editor()
    editor.view_document()
    editor.edit_document()

    # Запит ключа
    user_key = input("\nВведіть ліцензійний ключ для активації Pro версії: ")

    if user_key == license_key:
        editor = ProEditor()
        print("✅ Активація успішна! Ви використовуєте Pro версію.")
        editor.view_document()
        editor.edit_document()
    else:
        print("❌ Невірний ключ. Ви залишаєтесь у безкоштовній версії.")


if __name__ == "__main__":
    main()
