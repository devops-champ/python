#print the following pattern using nested while loop
"""
    2
    4 4
    6 6 6
    8 8 8 8
    10 10 10 10
    
"""


rows = 5

i =1

while i <= rows:
    j = 1
    while j <= i:
        print(i * 2, end=" ")
        j += 1
        
    i += 1    
    print()    



n = 6

for i in range(6):
    for j in range(i, n):
        if i % 2 == 0:
            print("*", end=" ")
        else:
            print("-", end=" ") 
    print()          
    
    
n =8
i =0


while i< n:
    j = 1
    while j <= n -i:
        if i % 2 == 0:
            print("*", end="")
        else:
            print("#", end="")
            
        j += 1
        
    print()
    
    i += 1        
                    