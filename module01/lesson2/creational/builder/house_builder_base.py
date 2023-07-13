from abc import ABC, abstractmethod


class HouseBuilder(ABC):
    @abstractmethod
    def destroy(self):
        pass

    @abstractmethod
    def build_basement(self, width, height):
        pass

    @abstractmethod
    def build_floors(self, floors_number):
        pass

    @abstractmethod
    def build_room(self, floor, square):
        pass

    @abstractmethod
    def build_roof(self, height, has_terrace):
        pass

    @abstractmethod
    def set_materials(self):
        pass
