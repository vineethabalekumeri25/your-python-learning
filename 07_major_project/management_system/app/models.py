import enum

# Enum for student courses
class Course(enum.Enum):
    PYTHON = "Python"
    DATA_SCIENCE = "Data Science"
    WEB_DEV = "Web Development"
    AI = "Artificial Intelligence"

# Simple OOP model for Student
class Student:
    def __init__(self, name: str, email: str, course: Course):
        self.name = name
        self.email = email
        self.course = course
