contacts = {}


def add_contact():
    global contacts
    name = input("Write name: ")
    if name not in contacts:
        ph_number = str(input("Write phone number: "))
        contacts[name] = ph_number
        print("Saved")
    else:
        print("The name already exists in the phonebook")


def del_contact(input_value):
    global contacts
    split_com = input_value.split()
    split_com.pop(0)
    name = " ".join(split_com)
    contacts.pop(name, "Name is missing")
    print("Contact is deleted")


def show_contacts(input_value):
    split_com = input_value.split()
    split_com.pop(0)
    contact = " ".join(split_com)
    if contact in contacts:
        print(f"Name: {contact}\nPhone number: {contacts.get(contact)}")
    else:
        print("Name is missing")


def stats():
    count_users = len(contacts)
    print('Number of contacts: ' + str(count_users))


def list_of_contacts():
    if len(contacts) > 0:
        count = 0
        for key, value in contacts.items():
            count += 1
            print(f"{count}. {key}")
    else:
        print("The contact list is empty")


while True:
    print("""\nEnter the command: 
- stats : number of contacts
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
