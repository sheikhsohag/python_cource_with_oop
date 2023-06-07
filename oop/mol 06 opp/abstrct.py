from abc import ABC, abstractmethod
                                #abc abstract base class
class Amimal(ABC):
    @abstractmethod    #enforce all derived class to have a eat method
    def eat(self):
        print('I need food')
    def move(self):
        pass


class Monkey(Amimal):
    def __init__(self,name) -> None:
        self.name = name
        self.category = 'Monkey'
        super().__init__()
    def eat(self):
        print('Hey na nana, I am eating banana')
    

layka = Monkey('lucky')
layka.eat()