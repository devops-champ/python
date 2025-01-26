import random 
#random.shuffle() requires mutable sequence to rearrange its elements.
my_list = list(range(20))

y=random.random()


print(y)

random.shuffle(my_list) 

print(my_list)
