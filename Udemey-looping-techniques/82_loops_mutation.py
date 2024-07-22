my_list = [1, 2, 3, 4, 5]

for num in my_list:
    my_list.remove(num)
    
    
print(my_list)    


#copy of the list
#[:] when used without specifying start and end indices, it will create a shaollow copy.

for num in my_list[:]:
    my_list.remove(num)
    
    
print(my_list)
    