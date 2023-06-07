from abc import ABC,abstractmethod

class User(ABC):
    def __init__(self,email,password) -> None:
        self.email = email
        self.password = password


class Customer(User):
    customer_list = []
    customers_email = []
    def __init__(self, email, password) -> None:
        self.initial_amount = 0
        super().__init__(email, password)

    def create_new_account(self,customer):
        if customer in self.customers_email:
            print('the email already exists')
        else:
            self.customer_list.append(customer)
            self.customers_email.append(customer.email)
            print('create account successfully')


        

    def login(self,email,password):
        if email in self.customers_email:
            print('Login successfully')
            return 1
        else:
            print('unknown user')
            return 0
        
    def order_place(self,order):
        pass

    def add_menoy(self,amount):
        self.initial_amount +=amount

    def Show_customer_list(self):
        for cum in self.customer_list:
            print(f'email: {cum.email} password: {cum.password}')


class Saler(User):
    def __init__(self, email, password) -> None:
        self.saler_list = []
        self.salers_email_list = []
        self.product_list = []
        self.saler_revenue = 0
        super().__init__(email, password)

    def create_account(self,customer):
        self.saler_list.append(customer)
        self.salers_email_list.append(customer.email)
        print('create account successfully')
    

    def login(self,email,password):
        if email in self.salers_email_list:
            print('Login successful')
            return 1
        else:
            print('unknown user')
            return 0
        
    def add_product(self,product):
        self.product_list.append(product)

    def Show_salar_list(self):
        for slar in self.saler_list:
            print(f'saler email: {slar.email} saler email: {slar.password}')
    
    def show_product(self):
        for item in self.product_list:
            print(f'Product name: {item.name} Product price: {item.price} and quantity: {item.quantity}')
        

class Product:
    def __init__(self,name,price,quantity) -> None:
        self.name = name 
        self.price = price
        self.quantity = quantity
        
    
    
    

            



        

