"""
клас для генерації парних чисел
"""


class NumbersGenerator:
    def __init__(self, start, end):

        if start % 2 != 0:
            self.current = start + 1
        else:
            self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            result = self.current
            self.current += 2
            return result


even_gen = NumbersGenerator(1, 15)
for number in even_gen:
    print(number)
