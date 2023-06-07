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

class Phone:
    def __init__(self,dual_sim) -> None:
        self.dual_sim=dual_sim

    def phone_call(self,number,text):
        return f'sending sms to: {number} with: {text}'

class Cemera:
    def __init__(self,pixel) -> None:
        self.pixel=pixel
    
    def change_lens(self):
        pass
        
