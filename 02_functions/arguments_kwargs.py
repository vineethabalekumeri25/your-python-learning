# 02_functions/arguments_kwargs.py
# Demonstrating *args and **kwargs

def show_args(*args):
    for arg in args:
        print("Arg:", arg)

def show_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

show_args(1, 2, 3)
show_kwargs(name="Alice", age=25)
