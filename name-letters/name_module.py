class NameInfo():
    def __init__(self, first_name, middle_name, last_name) -> None:
        self.first_name = first_name.title()
        self.middle_name = middle_name.title()
        self.last_name = last_name.title()
        self.full_name = self.first_name, self.middle_name, self.last_name

    def get_firstname(self) -> str:
        return self.first_name
    
    def get_middlename(self) -> str:
        return self.middle_name
    
    def get_lastname(self) -> str:
        return self.last_name
    
    def get_fullname(self) -> str:
        return self.full_name

    def get_all_letters(self) -> str:
        joined_names = "".join(self.full_name)

        letters = [letter.capitalize() for letter in joined_names if letter not in " '.-"]

        filtered_letters = sorted(list(set(letters)))
        
        # formatted_letters = [letter + ", " for letter in filtered_letters[:-1]]
        # formatted_letters.append(filtered_letters[-1])

        # all_letters = "".join(formatted_letters)

        # return all_letters
        
        return filtered_letters
