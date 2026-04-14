"""Цей модуль містить клас Animal для моделювання тварин та їхніх характеристик."""


class Animal:
    """Class representing a person"""

    def __init__(self, name, height, weight, color, voice):
        self.name = name
        self.height = height
        self.weight = weight
        self.color = color
        self.voice = voice

    def get_voice(self):
        """Function printing voice."""
        return self.voice

    def __str__(self):
        return (
            f"{self.name} is a {self.color} animal, "
            f"its height is {self.height} cm, "
            f"and it weighs {self.weight} kg."
        )


dog = Animal(name="Boba", height=60, weight=25, color="black", voice="Hoof-hoof!")
cat = Animal(name="Ryzhyk", height=30, weight=5, color="red", voice="Meiu-meiu!")
cow = Animal(name="Marta", height=150, weight=800, color="brown", voice="Moo-moo!")

print(dog)
print(f"And its voice is: {dog.get_voice()}\n")

print(cat)
print(f"And its voice is: {cat.get_voice()}\n")

print(cow)
print(f"And its voice is: {cow.get_voice()}\n")
