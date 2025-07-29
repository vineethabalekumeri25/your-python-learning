# 04_enums_and_modules/using_enums.py
from enum import Enum

class Status(Enum):
    NEW = 1
    IN_PROGRESS = 2
    DONE = 3

print("Status.NEW:", Status.NEW)