# my_string = 'hello'

# # my_list = []

# # for letter in my_string:
# #     my_list.append(letter)
# # print(my_list)    

# #or

# my_list_comp = [letter for letter in my_string]
# print(my_list_comp)


squares=[]

# for i in range(10):
#     squares.append(i**2)
# print(squares)

squares=[i**2 for i in range(10)]

print(squares)


# comd=[]

# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             comd.append((x,y))
            
# print(comd)


comd=[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]  
print(comd) 

# create a new list with the values doubled
vec = [-4, -2, 0, 2, 4] 

double =[]

for num in vec:
    double.append((num*2)) 
    
print(double)


double=[(num*2) for num in vec]       
print(double)

x=[(x, x**2) for x in range(6)]

print(x)

for y in list('word'):
    print(list(y))
    
your_list=  [y for y in 'word']   
print(your_list)



freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
fruit=[weapon.strip() for weapon in freshfruit]

print(fruit)