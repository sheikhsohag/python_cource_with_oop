
from user import Customer, Saler, Product

def main():

    #flag=True
    #while(flag==True):

        botton = input('Please press 1 for customer Or 2 for saler:', )

  
        if(botton == '1'):
            next = input("press 1 for Create new account Or 2 for LogIn:",) 
            email = input('Enter email: ', )
            password = input('Enter password: ',)
            customer = Customer(email,password)

            if next == '1':
                customer.create_new_account(customer)
                customer.Show_customer_list()
            else:
                 customer.login(customer,password)

        else:
             
            next = input("press 1 for Create new account Or 2 for LogIn:",) 
            email = input('Enter email: ', )
            password = input('Enter password: ',)
            saler1 = Saler(email,password)

            if next == '1':
                saler1.create_account(saler1)
                saler1.Show_salar_list()
            else:
                 saler1.login(saler1)
             

        #flag=False   
           
if __name__ == '__main__':
    main()