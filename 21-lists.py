my_list = [
    'string',
    25,
    3.2568
    
]

print(f'{my_list[2]:0.2f}')


#concatenate lists together

ur_list = [
    'one',
    'two',
    'three'
]

print(my_list + ur_list)


#update list
list3 = [1,2,[3,4,'hello']]

list3[2][2] = 'goodbye'

print(list3)

#append values to list
my_list.append('monkey')

print(my_list)

#remove the items in list
# ur_list.pop(1) #it's an inplace method. It won't return anything

# print(ur_list)

#sort

ur_list.sort() #it's an inplace method. It won't return anything

print(ur_list)


a_list = ['a', 'b', 'c', 'd', 'e', 'f']
a_list.reverse()     #it's an inplace method. It won't return anything

print(a_list)


#nesting lists

lst1 = [1,2,3]
lst2 = [4,5,6]
lst3 = [7,8,9]

matrix = [lst1, lst2, lst3]

print(matrix)

#call 2nd item in first matrix

print(matrix[0][1])