# set: unique items collection

#list --->[]
#tuple ---->()
#set--->{}

numbers = [1,2,3,1,2,3,4,6,7,4,5,6,7]
print(numbers)
numbers = set(numbers)

print(numbers)

numbers.add(34)
print(numbers)

numbers.remove(3)
print(numbers)


for item in numbers:
   if item%2==0 and item%3==0:
      print(item)