"""
Actors

    -- Passanger
    Elevator Car
    Floors
    Doors
    Button Panels
    Dispacther
    Elevator System
    Monitor System
    Indicator


"""


class Button(ABC):
    def press(self):
        pass
    def processed(self):
        pass

class HallButton(Button):
    pass

class ElevatorButton(Button):
    pass

class Door:
    def open(self):
        pass
    def close(self):
        pass
    pass

class InsideDoor(Door):
    pass

class OutsideDoor(Door):
    pass



