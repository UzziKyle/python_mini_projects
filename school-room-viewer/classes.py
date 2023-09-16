from os import system


class RoomViewer:
    def __init__(self) -> None:
        it_bldg = Building(name='IT Building', color='yellow', bldg_type='Laboratory', floor=2, permit=True)

        it_bldg_rooms = [
                    Room(name='CL1', color='white', area=100, rm_type='Lab', capacity=40, avail=True),
                    Room(name='CL2', color='white', area=80, rm_type='Lab', capacity=30, avail=True),
                    Room(name='CL3', color='white', area=100, rm_type='Lecture', capacity=40, avail=True),
                    Room(name='ACS', color='white', area=70, rm_type='Office', capacity=25, avail=True),
                    Room(name='SITE', color='white', area=70, rm_type='Office', capacity=25, avail=True),
                    Room(name='Chairperson\'s Office', color='white', area=70, rm_type='', capacity=25, avail=True),
                    Room(name='MTC1', color='white', area=100, rm_type='Lab', capacity=45, avail=True),
                    Room(name='MTC2', color='white', area=100, rm_type='Lab', capacity=45, avail=True),
                    Room(name='IT101', color='white', area=100, rm_type='Lab', capacity=45, avail=True),
                    Room(name='Old Faculty Room', color='white', area=100, rm_type='', capacity=45, avail=False),
                ]

        for room in it_bldg_rooms:
            room.assign_bldg(it_bldg)
        
        while True:
            system('cls')
            it_bldg.with_occupancy_permit()
            it_bldg.get_building_type()
            print('')

            print('View a room')
            [print(f'{num + 1}.) {room}') for num, room in enumerate(it_bldg_rooms)]
            user_input = int(input('Enter number: ').strip()) - 1

            if user_input < len(it_bldg_rooms) and user_input > 0:
            
                print('')
                it_bldg_rooms[user_input].is_available()
                it_bldg_rooms[user_input].get_capacity()

                input('Press \'Enter\' to continue...')


class Building:
    def __init__(self, name: str, bldg_type: str, color: str, floor: int = 1, permit: bool = False) -> None:
        self.name = name
        self.type = bldg_type
        self.color = color
        self.floor = floor
        self.permit = permit

    def __str__(self) -> str:
        return f'{self.name}'
    
    def __repr__(self) -> str:
        return f'{self.name}'

    def with_occupancy_permit(self) -> None:
        if not self.permit: return print(f'{self.name} has no permit.')

        print(f'{self.name} has permit.')
    
    def get_building_type(self) -> None:
        print(f'{self.name} is a {self.type} type.')
    

class Room:
    def __init__(self, name: str, color: str, area: float, rm_type: str, capacity: int = 10, avail: bool = True) -> None:
        self.name = name
        self.color = color
        self.area = area
        self.type = rm_type
        self.capacity = capacity
        self.avail = avail
        self.building = 'No assignment'

    def __str__(self) -> str:
        return f'{self.name}'
    
    def __repr__(self) -> str:
        return f'{self.name}'

    def is_available(self) -> None:
        if not self.avail: return print(f'{self.name} is not available.')
        
        print(f'{self.name} is available.')
    
    def assign_bldg(self, bldg) -> None:
        self.building = bldg

    def get_capacity(self) -> None:
        print(f'{self.name} has a capacity of {self.capacity} people.')
    

if __name__ == '__main__':
    room_viewer = RoomViewer()

    room_viewer