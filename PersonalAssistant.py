# Give the class a name
class PersonalAssistant:
  # Add an __init__ function here
  def __init__(self, todos, birthdays, contacts):
    self.todos = todos
    self.birthdays = birthdays
    self.contacts = contacts

   # Write the get_todo function
  def get_todo(self):
    return self.todos
    
  #Write add_todo function
  def add_todo(self, new_item):
    self.todos.append(new_item)
      
  #Write remove_todo function
  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      # Get the todo_item index in list
      index = self.todos.index(todo_item)
      # pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
      print("Todo is not in list!")
     
  
  #Write birthday functions
  def get_birthdays(self):
    return self.birthdays
        
  def get_birthday(self, name):
    if name in self.birthdays:
      return f"{name}'s birthday is on {self.birthdays[name]}."
    else:
      return f"Sorry, {name}'s birthday cannot be found."

  def add_birthday(self, name, date):
    if name in self.birthdays:
      return f"{name}'s birthday is already in the list."
    else:
      self.birthdays[name] = date
      return f"{name}'s birthday has been successfully added."

  def remove_birthday(self, name):
    if name in self.birthdays:
      self.birthdays.pop(name)
      return f"{name}'s birthday has been removed."
    else:
      return f"{name}'s birthday is not in the list and could not be removed."


  # Complete the contact function codes
  def get_contacts(self):
    return self.contacts
      
  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "Sorry, we don't have a contact with that name."
    
  def add_contact(self, name, position):
    if name in self.contacts:
      return f"{name}'s information is already in the list."
    else:
      self.contacts[name] = position
      return f"{name}'s information has been successfully added."

  def remove_contact(self, name):
    if name in self.contacts:
      self.contacts.pop(name)
      return f"{name}'s contact information has been removed."
    else:
      return f"{name} is not listed in contacts and could not be removed."
