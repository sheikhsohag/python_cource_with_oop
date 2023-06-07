#read only you can read, not setter a value of a method of private value
class user:
    def __init__(self,name,age,money) -> None:
        self._name=name
        self._age = age
        self.__money = money
    #def __repr__(self) -> str:
     # return f'{self.name}  {self.age} {self.money}'
    
    def age(self):                  # if attribute is protected or private then we can not access from any other  function. but you can access in this way 
       return self._age
    def money(self):
        return self.__money
    
    @property            #getter is  read only.  setter set kora jai
    def salary(self):
        return self.__money
                            #it is way to convert getter to setter
    @salary.setter
    def salary(self,value):
        if value < 0:
            return 'salary can not be nagetive'
        self.__money+=value
    
samsu = user('kopa', 21, 1200)
print(samsu.age())

print(samsu.salary)       #if we set @property then it is become a attribute not method. so print(samsu.money())  does not work print(samsu.money) it is right 

print(samsu.salary)
samsu.salary=1400     #increating value
print(samsu.salary)

        