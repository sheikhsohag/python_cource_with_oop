#base class/ parent class common attribute +functionality class
# derived class 

#here parameter are common attribute from all class
class Device:
    def __init__(self,brand,price,color,origin) -> None:
        self.brand=brand
        self.price=price
        self.color=color
        self.origin=origin
    def run(self):
        return f'phone tipa tipi kore'

class Laptop:
    def __init__(self,memory) -> None:
        self.memory=memory

    def coding(self):
        return f'larnign python and practicing'

class Phone(Device):
    def __init__(self,brand, price,color, origin, dual_sim) -> None:
        self.dual_sim=dual_sim
        super().__init__(brand, price,color,origin)

    def phone_call(self,number,text):
        return f'sending sms to: {number} with: {text}'
    
    def __repr__(self) -> str:
        return f'phone: {self.brand} price: {self.price} color: {self.color} origin: {self.origin} {self.dual_sim}'
        

class Cemera:
    def __init__(self,pixel) -> None:
        self.pixel=pixel
    
    def change_lens(self):
        pass
        
my_phone = Phone('iphone',120000,'silvar','china',True)
print(my_phone.brand)
print(my_phone)