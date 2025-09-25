from enum import Enum

class Course(Enum):
    MATH = "Mathematics"
    SCIENCE = "Science"
    HISTORY = "History"

# Usage
print(Course.MATH)          # Course.MATH
print(Course.MATH.value)    # Mathematics
