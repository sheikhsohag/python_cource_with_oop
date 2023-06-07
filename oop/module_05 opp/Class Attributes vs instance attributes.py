class Shop:
    cart = []       # class atribute as a result it is share all sohag and shohel both 
    def __init__(self,buyer):
        self.buyer=buyer

    def add_to_cart(self,item):
        self.cart.append(item) 

sohag = Shop('sohag ali')
sohag.add_to_cart('shoes')
sohag.add_to_cart('phone')
print(sohag.cart)

shohel = Shop('shohel phn')
shohel.add_to_cart('new_phone')
print(shohel.cart)


class Shop:
                                    # intance atribute as a result it is share indivial sohag and shohel both 
    #mall = 'jammuna'
    def __init__(self,buyer):
        self.buyer=buyer
        self.cart = []  

    def add_to_cart(self,item):
        self.cart.append(item) 

sohag = Shop('sohag ali')
sohag.add_to_cart('shoes')
sohag.add_to_cart('phone')
print(sohag.cart)

shohel = Shop('shohel phn')
shohel.add_to_cart('new_phone')
print(shohel.cart)