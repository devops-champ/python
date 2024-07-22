#lambda arguments: expression
#----> it can take multiple arguments

#few examples:

add = lambda x,y: x + y
print(add(5, 3))


my_list = [('apple', 2), ('banana', 1), ('cherry', 3)]
s_list = sorted(my_list, key=lambda x: x[-1])

print(s_list)


#from the course
d_list = ["C", "a", "B", "z"]

print(sorted(d_list, key=lambda x: x.lower()))