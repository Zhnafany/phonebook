import os
import dictionary from . as book

def main_loop():
    while True:
        try:
            clearConsole()
            menu()
            select_action()
        except KeyError as e:
            print(e)
        press_to_continue()

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def menu():
    """
    print menu to iteract
    """
    print("Contacts book(Name Phone)")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. List")
    print("6. Quit")

def select_action():
    """
    Get action from input
    @raise keyError: wrong input
    """
    action = int(input())
    if (action == 1):
        create()
    elif (action == 2):
        read()
    elif (action == 3):
        update()
    elif (action == 4):
        delete()
    elif (action == 5):
        contact_list()
    elif (action == 6):
        quit()
    else:
        raise KeyError("Wrong input. Try again.")

def create():
    """
    get contact, add contact, print result
    """
    contact = get_contact()
    book.add(contact[0], contact[1])
    print(f"Added {contact[0]} {contact[1]}")

def get_contact():
    """
    get input(name and phone) from console
    """
    input_data = input("Enter name and phone(Name 1111111111): ")
    contact = input_data.split()
    if len(contact) is not 2:
        raise KeyError("Wrong input. Try again.")
    return contact 

def read():
    """
    get name from console, get phone from book, print result
    """
    name = input("Enter name: ")
    phone = book.get(name)
    print(f"{name} {phone}")

def update():
    """
    get new contact data, update it, print info
    """
    contact = get_contact()
    book.update(contact[0]) = contact[1]
    print("Updated...")

def delete():
    """
    get name from iput, delete contact, print info
    """
    name = input("Enter name: ")
    book.delete(name)
    print(f"{name} was deleted..")

#better not use list name, because it is name of type data
def contact_list():
    """
    print list of contact book
    """
    book.list()
    for key, val in contact_book.items():
        print(f"{key} {val}")

def press_to_continue():
    """
    get enter to continue
    """
    print("Press enter to continue...")
    input()

def quit():
    clearConsole()
    exit()

main_loop()
