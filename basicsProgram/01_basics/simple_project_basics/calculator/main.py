# 01_basics/simple_project_basics/calculator.py
# Simple calculator with basic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

print("Add:", add(4, 2))
print("Subtract:", subtract(4, 2))
print("Multiply:", multiply(4, 2))
print("Divide:", divide(4, 2))