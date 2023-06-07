class Shop:
    def __init__(self,name):
        self.name=name
        self.goods=[]
        self.name_of_product = []

    def add_product(self,name,price,weight):
        self.name_of_product.append(name)
        product = Product(name,price,weight)
        self.goods.append(product)
    

    def buy_product(self,name,price,weight):
        if name in self.name_of_product:
            for item in self.goods:
                if name==item.name:
                    if weight<=item.weight:
                        print('congress')
                    else:
                        print('not sufficient product')    
            
        else:
            print('unavilable the product')
            
    def __repr__(self) -> str:
        for item in self.goods:
            print(item)
        return 'All done for now'

class Product:
    def __init__(self,name,price,weight) ->str:
        self.name=name
        self.price=price
        self.weight=weight

    def __repr__(self) -> str:
        return f'name: {self.name} price: {self.price} weight: {self.weight}'

shop = Shop('ali baba Shop')

shop.add_product('alu',30,20)
shop.add_product('potol',30,20)
shop.add_product('begun',30,20)
print(shop)
print(shop.buy_product('alu',30,2))

        