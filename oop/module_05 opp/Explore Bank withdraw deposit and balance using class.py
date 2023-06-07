class bank:
    def __init__(self,balance):
        self.balance=balance
        self.min_withdraw = 100
        self.max_withdraw =100000
    
    def get_balace(self):
        return self.balance
    
    def deposite(self,amount):
        if amount>0:
            self.balance+=amount
    def withdraw(self,amount):
        if amount < self.min_withdraw:
            return f'fokira. you can not withdraw below {self.min_withdraw}'
        elif amount > self.max_withdraw:
            return f'bank fokir hoi jabe jodi ar theke {self.max_withdraw} beshi nish '
        else:
            return f'ne tor taka {self.balance}'
        

brac = bank(150000)
print(brac.withdraw(12))
print(brac.withdraw(10000000))
print(brac.withdraw(1234))





class sonali_bank:

    def __init__(self,balance):
        self.balance=balance
        self.lower=100
        self.upper=1000000
    def deposite(self,amount):
        if amount > 0:
            self.balance+=amount
    def current_balance(self):
        return self.balance
    def withdraw(self,amount):
        if amount < self.lower:
            print('fokir taka pabi na')
        elif amount > self.upper:
            print('boro lok bank a ato tk nai')
        else:
            print('ne tor tk {amount}')
            self.balance-=amount
            print(f'current balance is {self.balance}')

brac = sonali_bank(150000)
print(brac.withdraw(12))
print(brac.withdraw(10000000))
print(brac.withdraw(1234))

