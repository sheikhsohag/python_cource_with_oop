class Shopping:
    cart = []   #class atribute #static attribute    #likely clobal variable 
                #static atrinute
    origin = 'china'

    def __init__(self,name,location) ->None:
        self.name='name'    #instance attribute
        self.location='location'

    def purchase(self, item, price, amount):
        remaining = amount-price
        print(f'buying: {item}, for price: {price}, and ramaining: {remaining}')
    @classmethod                                    #@classmethod    @ ata koi decorator   
    def dekhi(self,item):
        print('kinbuna kintu dekhbo',item)
    @staticmethod
    def multiply(a,b):  #@staticmethod it is same as ordinary function it can not access instance value, classsmethod can be access instance value
        ans = a*b
        print(ans)



#Shopping.purchase('a',3,4,5)
basundhora = Shopping('alu', 'unknown')

#bas = basundhora.purchase('lungi', 250, 3)  #class method

#Shopping.dekhi('item nai')    #if i do not decleare classmethod then we must be provided greater than one item but now it is not
                              #this system is called instance method
Shopping.multiply(5,6)   #staticmethod
#basundhora.multiply(4,5)




