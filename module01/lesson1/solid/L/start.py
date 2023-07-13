from abc import ABC, abstractmethod


class Member(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def save_database(self):
        pass

    @abstractmethod
    def pay(self):
        pass

class Teacher(Member):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id

    def save_database(self):
        print("Saving teacher data to database")

    def pay(self):
        print("Paying")


class Manager(Member):
    def __init__(self, name, age, manager_id):
        super().__init__(name, age)
        self.manager_id = manager_id

    def save_database(self):
        print("Saving manager data to database")

    def pay(self):
        print("Paying")


class Student(Member):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def save_database(self):
        print("Saving student data to database")

    def pay(self):
        raise NotImplementedError("It is free for students!")
