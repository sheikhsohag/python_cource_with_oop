
balance = 3000

def buy_things(item,price):
    global balance
    var = balance-1200
    print(var)
    print('balance inside the function', balance)
    return 12

buy_things('sunglass', 1000)