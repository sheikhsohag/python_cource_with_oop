

class Animal:
    def __init__(self,name) -> None:
        self.name=name
    def make_sound(self):
        print('animal making some sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('meow meow')
class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('ghew ghew')

class goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
        

don = Cat('real')

don.make_sound()

dog = Dog('boss')
dog.make_sound()

mess = goat('chagol')
mess.make_sound()