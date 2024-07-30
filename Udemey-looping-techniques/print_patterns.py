

n = 5

'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    
    print()

print()    
print("placeholder")
print()

'''
* * * * * 
* * * * 
* * * 
* * 
*
'''
    
for i in range(n):
    for j in range(i, n):
        print('*', end=" ")
    
    print()    
    
print()    
print("placeholder")
print()


"""
          * 
        * * 
      * * * 
    * * * * 
  * * * * *
"""    
    
for i in range(n):
    for space in range(i, n):
        print(" ", end=" ")
        
    for ast in range(i+1):
        print("*", end=" ")
        
    print() 
    
    
print()    
print("placeholder")
print()

'''
  * * * * * 
    * * * * 
      * * * 
        * * 
          *
'''

for i in range(5):
    for space in range(i+1):
        print(" ", end=" ")
        
    for ast in range(i, n):
        print("*", end=" ")    
        
    print()
    
    
print()    
print("placeholder")
print()

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

n = 5

for i in range(n+1):
    for j in range(1, i+1):
        print(j, end=" ")
        
    print()                              