# A program that asks for the full name of the user and then returns the letters contained in the name
import name_module as nm

# Input
first_name = input("Enter your first name: ").strip()
middle_name = input("Enter your middle name: ").strip()
last_name = input("Enter your last name: ").strip()

name = nm.NameInfo(first_name, middle_name, last_name)

# Process and Output
print(name.get_fullname())

print("\nYour name consists of letters {}.".format(name.get_all_letters()))
