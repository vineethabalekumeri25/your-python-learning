# 04_enums_and_modules/simple_project_enums/status_tracker.py
from enum import Enum

class TaskStatus(Enum):
    PENDING = "Pending"
    COMPLETE = "Complete"

tasks = {"Task1": TaskStatus.PENDING, "Task2": TaskStatus.COMPLETE}

for task, status in tasks.items():
    print(f"{task}: {status.value}")