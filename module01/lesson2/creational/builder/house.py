import json


class House:
    def __init__(self):
        self.height = None
        self.width = None
        self.materials = []
        self.has_terrace = False
        self.rooms = []
        self.floors_number = None
        self.roof_height = None

    def __str__(self):
        return json.dumps(self.__dict__)
