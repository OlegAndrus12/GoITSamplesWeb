from abc import ABC, abstractmethod
import time
import copy

class Prototype:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    @abstractmethod
    def clone(self):
        pass
    
    def __str__(self):
        return f"{self.name} {self.surname}"


class GoalKeeper(Prototype):
    def __init__(self, name, surname, defense):
        super().__init__(name, surname)
        self.defense = defense
    
    def clone(self):
        return GoalKeeper(self.name, self.surname, self.defense)

    def __str__(self):
        return f"GoalKeeper : {super().__str__()} | defense : {self.defense}"
    
    
class HalfBack(Prototype):
    def __init__(self, name, surname, speed):
        super().__init__(name, surname)
        self.speed = speed
    
    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Halfback: {super().__str__()} | speed : {self.speed}"
    
    
if __name__ == "__main__":
    players = [GoalKeeper("Ivan", "Petrenko", 12),  HalfBack("Mykola", "Ivanovych", 30)]
    # let's clone the players
    for i in players:
        print(f"Original object ==> {str(i)} with id {id(i)}")
        cloned_object = i.clone()
        print(f"Copied object ==> {str(cloned_object)} with id {id(cloned_object)}")
        del cloned_object
        print()
