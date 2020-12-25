# Python
#Suppose we have a file (module) with the following
class definition
module variable 1 last_id = -1
class AddressBook()
def __init__(self):
self.dblist = []
def add_contact(self, name, email):
global last_id last_id += 1
contact = [last_id, name, email]
self.dblist.append(contact)
def print_list(self):
for c in self.dblist:
print(c[0])
 #idnum print(c[1])
 #name print(c[2])
#email print("\n")
#end
AdressBook As you can see we are storing contacts in a list of three elements [id, name, email]
and then storing all of these contacts in a list. Defining a subclass of AddressBook that optionally includes an age for each contact.
Just store it as the fourth element of the contact list.
2 Call the __init__ method of the superclass in the subclass init method.
 Define a print_list method that prints the age of the contact, if present, and prints the list sorted alphabetically by name.
Define a method to acccept a string and print all the contacts whose name contains that substring.
 If there is no match, return None.
