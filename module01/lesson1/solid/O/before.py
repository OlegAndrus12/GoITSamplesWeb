from math import pi


class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Circle:
    def __init__(self, radius):
        self.radius = radius


def total_area(shapes):
    sum = 0
    for el in shapes:
        if isinstance(el, Rect):
            sum += el.width * el.height
        if isinstance(el, Circle):
            sum += el.radius ** 2 * pi
    return sum


if __name__ == '__main__':
    shapes = [Rect(10, 10), Circle(5), Rect(4, 5), Rect(3, 3), Circle(3)]
    area = total_area(shapes)
    print(area)

