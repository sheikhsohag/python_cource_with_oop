class Shop:
    def __init__(self,name) -> None:
        self.name=name
        self.goods=[]

    def add_product(self,name,price,weight):
        product = self.make_product(name,price,weight)
        self.goods.append(product)

class Product:
    def __init__(self,name) -> None:
        self.name=name

    def make_product(self,name,price,weight):
        return {'name':name,'price':price,'weight' = weight}

shop = 

        