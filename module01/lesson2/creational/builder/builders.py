from house_builder_base import HouseBuilder
from house import House


class HobbitHouseBuilder(HouseBuilder):
    def __init__(self):
        self.__house = House()
        self.__square = 0

    def destroy(self):
        self.__house = House()
        self.__square = 0

    def get_house(self):
        return self.__house

    def get_square(self):
        return self

    def build_basement(self, width, height):
        self.__house.width = width
        self.__house.height = height
        self.__square += width * height
        return self

    def build_floors(self, floors_number):
        self.__house.floors_number = floors_number
        return self

    def build_room(self, floor, square):
        self.__house.rooms.append((floor, square))
        return self

    def build_roof(self, height, has_terrace):
        self.__house.roof_height = height
        self.__has_terrace = has_terrace
        return self

    def set_materials(self, materials):
        self.__house.materials = materials
        return self


class MordorHouseBuilder(HouseBuilder):
    pass
