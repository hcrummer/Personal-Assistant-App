#imports PersonalAssistant.py file
import json
from PersonalAssistant import PersonalAssistant

#ADD CODE: open JSON file and pass data to PersonalAssistant class

with open("todo.json", "r") as todos, open("birthdays.json", "r") as birthdays, open("contacts.json", "r") as contacts:
  todo_list = json.load(todos)
  birthday_list = json.load(birthdays)
  contact_list = json.load(contacts)
  assistant = PersonalAssistant(todo_list, birthday_list, contact_list)
  
done = False

while not done:
    user_command = input(
        """
How can I help you?

    **** To-dos *****
    1: Add a to-do
    2: Remove a to-do
    3: Get to-do list
    **** Birthdays ****
    4: Get Birthday
    5: Add Birthday
    6: Remove Birthday
    **** Contacts ****
    7: Get a Single Contact
    8: Add a Contact
    9: Delete a Contact

    Select a number or type 'Exit' to quit: 
    
    """
    )
    # Add Todo
    if user_command == "1":
        user_input = input("Item to add to to-do list: ")
        assistant.add_todo(user_input)
    # Remove Todo
    elif user_command == "2":
        print(f"Your current todos: {assistant.get_todo()}")
        user_input = input("Item to remove from to-do list: ")
        print(f"\n {assistant.remove_todo(user_input)}")
    # Get Todo
    elif user_command == "3":
        print("\nYour to-do list")
        print(f"\n {assistant.get_todo()}")
    elif user_command == "4":
        print("\nYour birthday list")
        for name in assistant.get_birthdays():
            print(name)
        bday_name = input("\nPlease enter a name from the list: ")
        print(f"\n{assistant.get_birthday(bday_name)}")
    elif user_command == "5":
        name = input("Name of the person: ")
        birthday = input("Their birthday (ex: 08/18/2000): ")
        print(f"{assistant.add_birthday(name, birthday)}")
    elif user_command == "6":
        print("Your birthday contacts: \n")
        for name in assistant.get_birthdays():
            print(name)
        remove_bday = input("\nPlease enter a name from the list that you would like to remove: ")
        print(f"\n{assistant.remove_birthday(remove_bday)}")
    elif user_command == "7":
        print("\nYour contact list")
        for name in assistant.get_contacts():
            print(name)
        contact_name = input("\nPlease enter a name from the list: ")
        print(f"\n{assistant.get_contact(contact_name)}")
    elif user_command == "8":
        name = input("Name of the person: ")
        position = input("Please enter their work position: ")
        print(f"\n{assistant.add_contact(name, position)}")
    elif user_command == "9":
        print("Your contacts: \n")
        for name in assistant.get_contacts():
            print(name)
        remove_contact = input("\nPlease enter a name from the list that you would like to remove: ")
        print(f"\n{assistant.remove_contact(remove_contact)}")
    elif user_command == "exit" or user_command == "Exit" or user_command == "EXIT":
        done = True
        print("\nGoodbye, see you soon!")
    else:
        print("\nNot a valid command.")

# ADD CODE: write data to JSON file
with open("todo.json", "w") as write_todos, open("birthdays.json", "w") as write_birthdays, open("contacts.json", "w") as write_contacts:
  json.dump(assistant.get_todo(), write_todos)
  json.dump(assistant.get_birthdays(), write_birthdays)
  json.dump(assistant.get_contacts(), write_contacts)
