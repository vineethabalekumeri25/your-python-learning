class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade   # private variable

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade")

    def get_grade(self):
        return self.__grade

    def display_info(self):
        print(f"Student: {self.name}, Grade: {self.__grade}")


# Usage
s1 = Student("Alice", 85)
s1.display_info()     # Student: Alice, Grade: 85

s1.set_grade(95)
s1.display_info()     # Student: Alice, Grade: 95

s1.set_grade(150)     # Invalid grade
print(s1.get_grade()) # 95
