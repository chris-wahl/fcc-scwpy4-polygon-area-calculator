from typing import Union


class Rectangle:
    width: float
    height: float

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width: float):
        self.width = width

    def set_height(self, height: float):
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        return '\n'.join([
            '*' * self.width for _ in range(self.height)
        ]) + '\n'

    def get_amount_inside(self, shape: Union['Square', 'Rectangle']) -> int:
        shape_area = shape.get_area()
        return int(self.get_area() / shape_area)


class Square(Rectangle):

    def __init__(self, side: float):
        super().__init__(side, side)

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, side: float):
        self.set_width(side)
        self.set_height(side)
