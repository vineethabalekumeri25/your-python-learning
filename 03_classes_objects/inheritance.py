# 03_classes_objects/inheritance.py
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()
a = Animal()
a.speak()