import json

# class Student:
#     tiredness = 0
#     progress = 0
#
#     def __init__(self, tiredness, progress):
#         self.tired = tiredness
#         self.progress = progress
#
#     def study(self):
#         if self.tiredness < 85:
#             self.tiredness += 15
#         else:
#             self.tiredness = 100
#         self.progress += 10
#
#     def rest(self):
#         if self.tiredness > 5:
#             self.tiredness -= 5
#         else:
#             self.tiredness = 0
#
#     def is_done(self):
#         if self.progress >= 100:
#             print("Студент выучился")
#         else:
#             print("Студент учится")
#
#     def demotivated(self):
#         return self.tiredness > 100
#
#
# student_ilya = Student(tiredness=15, progress=10)
# student_dima = Student(tiredness=5, progress=20)
#
#
# print(student_ilya.tiredness)
# print(student_ilya.progress)
# student_dima.study()
# for i in range(2):
#     student_ilya.study()
# print(student_ilya.tiredness, student_ilya.progress)
# print(student_dima.tiredness, student_dima.progress)


class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def make_noise(self):
        print("Grrr")

    def __inner_method(self):
        print("Выполнился внутренний метод")

    def get_name(self):
        self.inner_method()
        return self.name


class Cat(Animal):
    def make_noise(self):
        print("Meow")


class Dog(Animal):
    def make_noise(self):
        print("Gav")


animal = Animal("Барсик", 100)
animal.inner_method()


cat1 = Cat(name="Barsik", health=100)
dog1 = Dog(name="Sharik", health=200)


print(cat1.name)
print(cat1.make_noise())
print(dog1.name)
print(dog1.make_noise())




