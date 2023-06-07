"""#base class 

class BaseClass:
    pass

class DerivedClass(BaseClass):    #derived class or child class
"""


class Vehicle:
    def __init__(self,name,price) -> None:
        self.name=name
        self.price=price
    def move(self):
        pass
    def __repr__(self) -> str:
        return f'name: {self.name} price: {self.price}'


class Bus(Vehicle):
    def __init__(self, name, price,seat) -> None:
        self.seat=seat
        super().__init__(name, price)
    def __repr__(self) -> str:
        return super().__repr__()


class Truck(Vehicle):
    def __init__(self, name, price,weight) -> None:
        self.weight
        super().__init__(name, price)

class PickUpTrack(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)


class ACBus(Bus):
    def __init__(self, name, price, seat,temperature) -> None:
        self.temperature=temperature
        super().__init__(name, price, seat)
    def __repr__(self) -> str:
        print(f'{self.seat}')
        return super().__repr__()


green_line = ACBus('green', 500000000, 22,16)
print(green_line)
       