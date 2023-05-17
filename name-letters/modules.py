class Modules():
    def __init__(self) -> None:
        pass 

    def list_to_set(list = list) -> set:
        return set(list)

    def get_letters(list = list) -> list:
        letters = []
        for name in list:
            for character in name:
                if character not in " '.-":
                    letters.append(character)
        
        return letters
    
    def set_to_list(set = set) -> list:
        return list(set)