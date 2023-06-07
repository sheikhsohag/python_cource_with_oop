def full_name(first,last):
    name = f'full name is: {first} {last}'
    return name;

# take parameters in order 

name = full_name('alu','kaa')
print(name)


def sum(nums,num):
    a = nums+num
    s = nums-num
    m=nums*num
    d=nums/num
    return a,s,m,d

ans = sum(4,2)
for val in ans:
    print(val)

