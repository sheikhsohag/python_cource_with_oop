
from user import Customer, Saler, Product

def main():

    #flag=True
    #while(flag==True):
           
    email = input('Enter customer email: ', )
    password = input('Enter customer password: ',)
    customer1 = Customer(email,password)

    customer1.create_new_account(customer1)
    #customer1.Show_customer_list()

    email = input('Enter custormer email: ', )
    password = input('Enter customerpassword: ',)
    customer2 = Customer(email,password)

    customer2.create_new_account(customer2)
    customer2.Show_customer_list()
    
    email = input('Enter saler email: ', )
    password = input('Enter saler password: ',)
    salar1 = Saler(email,password)

    salar1.create_account(salar1)
    salar1.Show_salar_list()
    


    
           
if __name__ == '__main__':
    main()