import random
"""
Name Generator made by Jonah Fritz
Uses 2 files, names.txt and surnames.txt. Both files should contain only names separated by spaces.
The user can run the program to have a random name/surname pair generated.
Also, there are commands to be used by the user for adding surnames or names to the text files.
Useful for RPG character creation.
"""

"""
Opens a file and returns a list of every word separated by spaces within that file.
"""
def read_text(filename):
    appended_text = []
    with open(filename) as file:
        for line in file:
            words = line.split()
            for word in words:
                appended_text.append(word)
    return appended_text

def create_random_name():
    names = read_text("names.txt")
    surnames = read_text("surnames.txt")
    random_name = names[random.randint(0, len(names) - 1)]
    random_surname = surnames[random.randint(0, len(surnames) - 1)]
    return random_name + " " + random_surname

def main():
    print(create_random_name())

main()
