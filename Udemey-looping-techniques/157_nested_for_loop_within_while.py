x= 5

while x < 9:
    for i in range(3): #the nested for loop completes three iterations per iteration of the while loop
        print("Hello")
        
    x += 2
    
    
n = 4
d = 1

for i in range(1, n+1):
    #print spaces
    for j in range(n-i):
        print(end = "")
    
    #print numbers   
    for k in range(i):
       
        print(d, end =" ")
        d+=1
    print()     
    
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]




     
        



z = [[1,2], 2, [3,4,5]]

for index, value in enumerate(z):
    if isinstance(value, list):
        for indexin, digits in enumerate(value):
            value[indexin] = digits * 10
    else:
        z[index] = value * 10
        
print(z)





rows =5 

for i in range(rows):
    print("========")
    for j in range(rows-i):
        if j % 2== 0:
            print("*", end="")
        else:
            print("-", end="")
            
    print()                    