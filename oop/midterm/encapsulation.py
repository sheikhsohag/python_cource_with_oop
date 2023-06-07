def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func

closure_func = outer_func(10)

print(closure_func(5)) 


def Outer_function(x):
    def Inner_function(y):
        return x*y
    return Inner_function
closure_func = Outer_function(4)
print(closure_func(5))
print(closure_func(20))
