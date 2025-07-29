# 03_classes_objects/class_definition.py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

p = Person("Alice", 25)
p.greet()