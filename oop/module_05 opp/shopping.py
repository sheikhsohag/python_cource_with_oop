class Shopping:
    def __init__(self, name):
        self.name=name
        self.cart=[]

    def add_to_cart(self,item,price,quantity):
        product = {'item':item, 'price':price,'quantity':quantity}
        self.cart.append(product)
    
    #def remove_item(self,item):
        #self.cart.pop("item")
        

    def checkout(self,amount):
        total=0
        for item in self.cart:
            total += item['price'] * item['quantity']
        if total<amount:
            print('total prince', total)
        elif total>amount:
            print('please provide sufficient balance')



sohag = Shopping('Sohag')
sohag.add_to_cart('alu',50,2)
sohag.add_to_cart('potol',40,4)
sohag.add_to_cart('rice',20,5)
print(sohag.cart)
sohag.checkout(1000)

sohag.cart.pop(0)

sohag.checkout(1000)



