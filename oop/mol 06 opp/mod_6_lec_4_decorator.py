import math
import time
def timer(func):
    def inner(*args,**kwargs):
        start = time.time()
        print('time started')

        func(*args,**kwargs)
        print('time ended')
        end = time.time()


        print(f'start time is: {start}, and end time is: {end}, and total time taken {end-start}')

    return inner

@timer
def get_factorial(n):
    print('factorial starting')    #esiar way to decleare user decorator
    result = math.factorial(n)
    print(f'factorial of {n} is: {result}')

get_factorial(n=85)

#timer()()

#timer(get_factorial)()     #it complex system to decleare user decorator