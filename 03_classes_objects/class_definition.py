# 03_classes_objects/class_definition.py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

p1 = Person("Alice", 25)
p2 = Person("Bob", 24)

p1.greet()
p2.greet()