# 03_classes_objects/simple_project_oop/student_tracker.py
class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0

s = Student("John")
s.add_mark(85)
s.add_mark(90)
print(s.name, "Average:", s.average())