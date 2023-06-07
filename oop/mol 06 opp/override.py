class person:
    def __init__(self,name,age,height,weight) ->None:
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def eat(self):
        print('vat mangso polau korma')
    def exercise(self):
        raise NotImplementedError


class Cricketer(person):
    def __init__(self, name, age, height, weight,team) -> None:
        super().__init__(name, age, height, weight)
        self.team=team
        super().__init__(name,age,height,weight)
        #override beacuse of same method include patent class but now it is consider below method 
    def eat(self):
        print('vagitable')

    def exercise(self):
        print('gym a jabo na')
    def __add__(self,other):
        return self.age + other.age     # over load method,please google, python dunder methon, if we add, mul ,sub there age.python ducumentaion
    #for add, operator overload
    def __mul__(self,other):
        return self.age*other.age
    def __len__(self):
        return self.hight
    def __gt__(self, other):
        return self.height>other.height




sakib = Cricketer('sakib',38,78,91,'BD')
mushi = Cricketer('mushi',36,65,78,'BD')
mash = Cricketer('mash',40,78,90,'BD')
#sakib.eat()
#sakib.exercise()
print('sakib'+'rakib')
print([1,2,3,4,]+[3,4,5,6])

print(sakib+mushi)
print(sakib*mushi)
print(mushi.height)
print(sakib>mushi)