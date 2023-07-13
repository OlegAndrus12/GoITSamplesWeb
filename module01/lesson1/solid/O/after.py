from math import pi


class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_of(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area_of(self):
        return self.radius ** 2 * pi


def total_area(shapes):
    sum = 0
    for el in shapes:
        sum += el.area_of()
    return sum


if __name__ == '__main__':
    shapes = [Rect(10, 10), Circle(5), Rect(4, 5), Rect(3, 3), Circle(3)]
    area = total_area(shapes)
    print(area)

