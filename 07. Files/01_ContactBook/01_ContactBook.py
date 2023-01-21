# 1. Use the file as a database to store phonebook entries from previous tasks.
#
# Your phonebook, previously contained in a dict, should be stored as text in JSON format.
# When closing the program and opening it again, all previous data should be available.

import json
import os


with open("contacts.json", "a+", encoding='utf-8') as file:
    is_empty = os.stat("contacts.json").st_size == 0
    if is_empty:
        file.write("{}")


def add_contact():
    with open("contacts.json", "r+") as file_data:
        our_contacts = json.loads(file_data.read())
        file_data.seek(0)

        name = input("Write name: ")

        if len(name.strip()) != 0:
            if name not in our_contacts:
                ph_number = str(input("Write phone number: "))

                our_contacts[name] = ph_number
                file_data.write(json.dumps(our_contacts))

                print("Saved")
            else:
                print("The name already exists in the phonebook")
        else:
            print("An empty line is entered.")


def del_contact(input_value):
    split_com = input_value.split()
    split_com.pop(0)
    name = " ".join(split_com)

    with open("contacts.json", "r+") as file_data:
        our_contacts = json.loads(file_data.read())
        our_contacts.pop(name, "Name is missing")

    with open("contacts.json", "w") as file_data:
        file_data.write(json.dumps(our_contacts))
        print("Contact is deleted")


def show_contacts(input_value):
    split_com = input_value.split()
    split_com.pop(0)
    contact = " ".join(split_com)

    with open("contacts.json", "r") as file_data:
        our_contacts = json.loads(file_data.read())
        if contact in our_contacts:
            print(f"Name: {contact}\nPhone number: {our_contacts.get(contact)}")
        else:
            print("Name is missing")


def stats():
    with open("contacts.json", "r") as file_data:
        our_contacts = json.loads(file_data.read())
        count_users = len(our_contacts)
        print('Number of contacts: ' + str(count_users))


def list_of_contacts():
    with open("contacts.json", "r") as file_data:
        our_contacts = json.loads(file_data.read())
        if len(our_contacts) > 0:
            count = 0
            for key, value in our_contacts.items():
                count += 1
                print(f"{count}. {key}")
        else:
            print("The contact list is empty")


while True:
    print("""\nEnter the command:
- stats : number of contacts
- list : list of contacts
- show <name> : detailed information by name
- add : add contact
- delete <name>: delete contact by name (key)
- exit : end the program
    """)

    command = input('> ')
    if command == 'stats':
        stats()
    elif command.startswith('show'):
        show_contacts(command)
    elif command == 'add':
        add_contact()
    elif command == 'list':
        list_of_contacts()
    elif command.startswith('delete'):
        del_contact(command)
    elif command == 'exit':
        break
    else:
        print("Invalid command")
