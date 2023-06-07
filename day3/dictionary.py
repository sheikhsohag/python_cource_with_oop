#key value pair 
#dictionry 
 #object
#hash table
#overlap with set
person = {'name' : 'sohag ali','addres' : 'kushtia','age' : 23,'job' : 'student'}   #declearation system is:  keys : value
print(person)

print(person['age'])

print(person.keys())  # only for keys

print(person.values()) #only for value

person['language']='bangla'   # add new value 

print(person)


person['addres']='dhaka' # for change value

print(person)

#in this way only print keys value 
for item in person:
    print(item)

#in this way we can get key and correspoding value

for key, value in person.items():
    print(key, value)