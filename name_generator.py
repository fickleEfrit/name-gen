"""
Name Generator made by Jonah Fritz
Uses 2 files, names.txt and surnames.txt. Both files should contain only names separated by spaces.
The user can run the program to have a random name/surname pair generated.
Also, there are commands to be used by the user for adding surnames or names to the text files.
Useful for RPG character creation.
"""

import random

#tuple of all user commands
COMMAND_LIST = ("stop", "add_name", "add_surname", "help", "random_name")

def read_text(filename : str) -> list:
    """
    Opens a file and returns a list of every word separated by spaces within that file.
    :param filename: the name of the file to be opened
    :return: list of words within filename separated by spaces
    """
    appended_text = []
    with open(filename) as file:
        for line in file:
            words = line.split()
            for word in words:
                appended_text.append(word)
    return appended_text

def create_random_name() -> str:
    """
    Creates a random name
    :return: A random name
    """
    names = read_text("names.txt")
    surnames = read_text("surnames.txt")
    random_name = names[random.randint(0, len(names) - 1)]
    random_surname = surnames[random.randint(0, len(surnames) - 1)]
    return random_name + " " + random_surname

def add_name(name : str):
    """
    Adds a name to names.txt
    :param name: name to be added to names.txt
    :return: None
    """
    with open("names.txt", "a") as file:
        file.write(" " + name + " ")

def add_surname(surname : str):
    """
    Adds a name to surnames.txt
    :param surname: surname to be added to surnames.txt
    :return: None
    """
    with open("surnames.txt", "a") as file:
        file.write(" " + surname + " ")



def main():
    command = ""
    while(command != "stop"):
        print("Enter a command, stop to exit")
        command = input()
        if command not in COMMAND_LIST:
            print("Unrecognized command, type help for command list.")
        #print list of commands
        elif(command == "help"):
            help_response = "Commands: "
            for str in COMMAND_LIST:
                help_response += str + " "
            print(help_response)
        #add a name
        elif(command == "add_name"):
            name_to_add = input("Enter name to add: ")
            add_name(name_to_add)
            print("Added " + name_to_add + " to names.txt")
        #add a surname
        elif(command == "add_surname"):
            surname_to_add = input("Enter surname to add: ")
            add_surname(surname_to_add)
            print("Added " + surname_to_add + " to names.txt")
        #generate a random name
        elif(command == "random_name"):
            print(create_random_name())
    print("Exiting.")
    exit()

main()
