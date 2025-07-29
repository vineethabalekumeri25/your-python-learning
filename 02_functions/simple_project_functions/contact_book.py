# 02_functions/simple_project_functions/contact_book.py
# Simple contact book

contacts = {}

def add_contact(name, number):
    contacts[name] = number

def view_contacts():
    for name, number in contacts.items():
        print(name, ":", number)

add_contact("Alice", "12345")
add_contact("Bob", "67890")
view_contacts()