class Person:
    def __init__(self) -> None:
        pass
    def print(self):
        print('All person')

class Old_person(Person):
    def __init__(self) -> None:
        super().__init__()
    def print(self):
        print('old_person')
    
class Retired_person(Old_person):
    def __init__(self) -> None:
        super().__init__()
    def print(self):
        print('retired_person')

person = Person()
person.print()

old_person = Old_person()
old_person.print()

retired_person = Retired_person()
retired_person.print()



    