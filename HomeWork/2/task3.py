"""Приклад множинного успадкування та MRO."""


class A:
    """Клас A."""

    def say(self):
        """Вивести ім'я класу."""
        print("Клас A")


class B(A):
    """Клас B, успадковує A."""

    def say(self):
        """Вивести ім'я класу."""
        print("Клас B")


class C(A):
    """Клас C, успадковує A."""

    def say(self):
        """Вивести ім'я класу."""
        print("Клас C")


class D(B, C):
    """Клас D, успадковує B і C."""


def main():
    """Основна логіка програми."""
    d = D()
    d.say()

    print("\nПорядок вирішення методів (MRO):")
    for cls in D.__mro__:
        print(cls)


if __name__ == "__main__":
    main()
