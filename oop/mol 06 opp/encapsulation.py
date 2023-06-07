class Bank:
    def __init__(self,holder_name,initial_deposit) -> None:
        self.holder_name=holder_name
        self.__balance = initial_deposit
    
    def deposite(self,amount):
        self.__balance+=amount

    def get_balance(self):
        return self.__balance
    
    def withdraw(self,amount):
        if self.__balance < amount:
            print('fokir')
        else:
            self.__balance=self.__balance-amount
            return f'remain {self.__balance} balace {amount}'


rafsun = Bank('chooto bro', 120000)
rafsun.deposite(1200)
print(rafsun.holder_name,rafsun.get_balance())
print(rafsun.withdraw(12000))



        