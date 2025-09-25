from enum import Enum

class Status(Enum):
    TODO = "To Do"
    IN_PROGRESS = "In Progress"
    DONE = "Done"

class Task:
    def __init__(self, title, status=Status.TODO):
        self.title = title
        self.status = status

    def update_status(self, new_status):
        if isinstance(new_status, Status):
            self.status = new_status
        else:
            print("Invalid status")

    def display(self):
        print(f"Task: {self.title} | Status: {self.status.value}")

# Usage
t1 = Task("Write report")
t1.display()                      # Task: Write report | Status: To Do

t1.update_status(Status.IN_PROGRESS)
t1.display()                      # Task: Write report | Status: In Progress

t1.update_status("Finished")      # Invalid status
