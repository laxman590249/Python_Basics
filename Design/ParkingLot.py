from abc import ABC
"""
Actors:
    ParkingLot
    Termninal (Gates)
    Parking assignment 
    Vehicle
    Payment
    Terrif Calculator
    Logger
"""
class ParkingSpot(ABC):
    id = None
    reserve = None

class HandicappedParkingSpot(ParkingSpot):
    pass

class CopactParkingSpot(ParkingSpot):
    pass

class LargeParkingSpot(ParkingSpot):
    pass

class MotorcycleParkingSpot(ParkingSpot):
    pass


class Terminal(ABC):
    def get_id(selp):
        pass

class EntryTerminal(Terminal):
    def get_ticket(self):
        pass

class ExitTerminal(Terminal):
    def accept_ticket(self):
        pass

class ParkingAssignmentStrategy:

    def get_parking_spot(self, terminal):
        pass

    def release_parking_spot(self, ParkingSpot):
        pass



class PaymentProcessor(ABC):
    def process(self, amount):
        pass

class CreditCardPaymentProcessor(PaymentProcessor):
    pass

class CashPayProcessor(PaymentProcessor):
    pass

class QRPayProcessor(PaymentProcessor):
    pass


class TerrifCalculator:
    def calculate_terrif(self, time, ParkingSpot):
        pass

class logger:
    def log_message(self, message):
        pass

class ParkingLotSystem: # (Singleton)

    pass

