"""Модуль для малювання різних геометричних фігур (коло, квадрат, трикутник, конус, параболоїд)."""

from PIL import Image, ImageDraw


class Shape:
    """Базовий клас для створення полотна та відображення зображень."""

    def __init__(self, width=400, height=400, color="white"):
        """Ініціалізувати нове зображення."""
        self.width = width
        self.height = height
        self.color = color
        self.image = Image.new("RGB", (width, height), color)
        self.draw = ImageDraw.Draw(self.image)

    def show(self):
        """Показати зображення."""
        self.image.show()


class Circle(Shape):
    """Клас для малювання кола."""

    def draw_circle(self, x, y, r, fill="blue"):
        """Намалювати коло з центром (x, y) та радіусом r."""
        self.draw.ellipse((x - r, y - r, x + r, y + r), fill=fill)


class Square(Shape):
    """Клас для малювання квадрата."""

    def draw_square(self, x1, y1, x2, y2, fill="green"):
        """Намалювати квадрат за координатами протилежних вершин."""
        self.draw.rectangle((x1, y1, x2, y2), fill=fill)


class Triangle(Shape):
    """Клас для малювання трикутника."""

    def draw_triangle(self, points, fill="red"):
        """Намалювати трикутник за списком вершин."""
        self.draw.polygon(points, fill=fill)


class Cone(Shape):
    """Клас для малювання конуса."""

    def draw_cone(self, x, y, r, h, fill="purple"):
        """Намалювати конус із центром основи (x, y), радіусом r та висотою h."""
        base = (x - r, y - r, x + r, y + r)
        self.draw.ellipse(base, outline=fill)
        self.draw.polygon([(x - r, y), (x + r, y), (x, y - h)], fill=fill)


class Paraboloid(Shape):
    """Клас для малювання параболоїда."""

    def draw_paraboloid(self, x, y, r, h, fill="orange"):
        """Намалювати параболоїд із центром основи (x, y), радіусом r та висотою h."""
        for i in range(h):
            k = (i / h) ** 2
            self.draw.ellipse(
                (x - r * k, y - i, x + r * k, y + i),
                outline=fill,
            )


def main():
    """Головне меню програми для вибору фігури."""
    while True:
        try:
            value = int(
                input(
                    "\nМЕНЮ:"
                    "\n\t1. Створити тло"
                    "\n\t2. Створити коло"
                    "\n\t3. Створити квадрат"
                    "\n\t4. Створити трикутник"
                    "\n\t5. Створити конус"
                    "\n\t6. Створити параболоїд"
                    "\n\t7. Вихід з програми"
                    "\nОберіть необхідний пункт меню: "
                )
            )

            if value == 1:
                shape = Shape()
                shape.show()

            elif value == 2:
                circle = Circle()
                circle.draw_circle(200, 200, 100)
                circle.show()

            elif value == 3:
                square = Square()
                square.draw_square(100, 100, 300, 300)
                square.show()

            elif value == 4:
                triangle = Triangle()
                triangle.draw_triangle([(200, 50), (50, 350), (350, 350)])
                triangle.show()

            elif value == 5:
                cone = Cone()
                cone.draw_cone(200, 300, 100, 150)
                cone.show()

            elif value == 6:
                paraboloid = Paraboloid()
                paraboloid.draw_paraboloid(200, 200, 100, 150)
                paraboloid.show()

            elif value == 7:
                print("Вихід з програми.")
                break

            else:
                print("❌ Невірний вибір. Спробуйте ще раз.")

        except ValueError:
            print("❌ Потрібно ввести число.")


if __name__ == "__main__":
    main()
