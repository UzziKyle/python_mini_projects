# A program that asks for the full name of the user and then returns the letters contained in the name
from modules import Modules as md  

# Input
first_name = input("Enter your first name: ").strip().lower()
middle_name = input("Enter your middle name: ").strip().lower()
last_name = input("Enter your last name: ").strip().lower()

full_name = [first_name, middle_name, last_name]

# Process and Output
sorted_name_letters = sorted(md.list_to_set(md.get_letters(full_name)))

letters_list = []
for items in sorted_name_letters:
    letters_list.append(items.capitalize())
    if items not in sorted_name_letters[-1]:
        letters_list.append(", ")

letters = "".join(letters_list)

print("\nYour name consists of letters {}.".format(letters))
