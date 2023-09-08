class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.my_dict = {1:big, 2:medium, 3:small}

    def addCar(self, carType: int) -> bool:
        if self.my_dict[carType] == 0: return False
        self.my_dict[carType] -= 1
        return True
