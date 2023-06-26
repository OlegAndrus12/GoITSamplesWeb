class Dog:
    def __init__(self, name):
        self._name = name
        self._sound = "Woof!"

    def speak(self):
        return self._sound


class Cat:
    def __init__(self, name):
        self._name = name
        self._sound = "Meow!"

    def speak(self):
        return self._sound


def get_pet(pet="dog"):
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets.get(pet, pets["dog"])


if __name__ == '__main__':

    d = get_pet("dog")
    print(d.speak())

    c = get_pet("cat")
    d = get_pet("crocodile")
    print(c.speak())
    print(d.speak())
