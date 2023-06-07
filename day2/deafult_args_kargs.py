def sum(num1, num2):
    return num1+num2
total = sum(12,23)
print(total)

#args

#tuple

def all_sum(*numbers):
    print(numbers)
    sum=0
    for nm in numbers:
        print(nm)
        sum+=nm
    print(sum)

print('print all sum = ',all_sum(24,13,23,46,46))