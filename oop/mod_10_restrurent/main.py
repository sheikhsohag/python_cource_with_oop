from Menu import Pizza, Burger, Drinks, Menu
from restaurant import Restaurant
from User import Chef, Manager,Server,Customer
from order import Order

def main():
    menu = Menu()
    pizza1 = Pizza('shutki Pizza', 600, 'large', ['shutki', 'onion'])
    menu.add_menu_item('pizza', pizza1)

    pizza2 = Pizza('alur vortar pizza',400, 'large', ['potato', 'onion', 'oil'])
    menu.add_menu_item('pizza', pizza2)

    pizza3 = Pizza('Dal pizza', 500, 'large', ['dal', 'oil'])
    menu.add_menu_item('pizza', pizza3)

    #add burger to the manu
    burger1 = Burger('Naga Burger',1000, 'chicken', ['bread','chili'])
    menu.add_menu_item('burger', burger1)

    burger2 = Burger('beef Burger',1200, 'beef', ['goru', 'bread','chili'])
    menu.add_menu_item('burger', burger2)


    coke = Drinks('Coke', 120, True)
    menu.add_menu_item('drinks', coke)

    coffee = Drinks('Coffee', 120, False)
    menu.add_menu_item('drinks', coffee)

    menu.show_menu()


    restaurant  =  Restaurant('sai baba restaurant', 2000, menu)

    manager = Manager('kala chan manager', 5, 'kala@chan.com','kaliapur',1500,'jan 1 2020','core')
    restaurant.add_employee('manager',manager)

    chef = Chef('Rustom Babu', 6, 'chupa@rustom.com', 'rustomnagor', 3500, 'feb 1 2020', 'Chef', 'everythings')
    restaurant.add_employee('chef', chef)

    server = Server('coto',6,'naijai@.com', 'restaurant', 200,'feb 4 2020', 'server')

    restaurant.add_employee('server',server)

    #show employees
    restaurant.show_employees()


    #add customar

    customer1 = Customer('sakib al hasan', 6, 'al hasan@.com', 'banani', 100000)
    
    order1 = Order(customer1,[pizza3, coffee])
    customer1.pay(order1)
    restaurant.add_order(order1)

    #customer one paying for order_1

    restaurant.receive_payment(order1, 2000,customer1)

    print(restaurant.revenue, restaurant.balance)


    customer2 = Customer('sakib', 6, 'hasan@.com', 'banani', 100000)
    
    order2 = Order(customer1,[pizza1, coke, pizza2,pizza3,pizza1])
    customer2.pay(order2)
    restaurant.add_order(order2)

    #customer one paying for order_1

    restaurant.receive_payment(order2, 20000,customer2)

    restaurant.pay_expense(restaurant.rent,'rent')

    print(restaurant.revenue, restaurant.balance, restaurant.expense)





if __name__ == '__main__':
    main()