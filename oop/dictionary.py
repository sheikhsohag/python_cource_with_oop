class User:
    def __init__(self,name,id,password) -> None:
        self.name = name 
        self.id = id
        self.password = password


class Shop():
    customer_list = {}
    salar_list = {}
    def __init__(self) -> None:
        pass

    def add_customer(self,id,custom):
        self.customer_list[id] = custom


    def show_customer(self):
        for person in self.customer_list:
            print(f'user id: {person}, user name: {self.customer_list[person].name} user_password: {self.customer_list[person].password}')


class Customer(User):
    def __init__(self, name, id, password) -> None:
        super().__init__(name, id, password)


customer1 = Customer('sohag',101,1234)
shop = Shop()

shop.add_customer(101,customer1)

customer2 = Customer('shohel', 102,2345)
shop.add_customer(102,customer2)

shop.show_customer()


    

        

