print(list(range(-3,3)))

print(list(range(2, -5)))

print(list(range(-5, -2)))

print(list(range(2, -5)))

#if start > stop with -ve step
print(list(range(7, 2, -2)))

print(list(range(1, 7, -2)))

n=4

for i in range(n, -1, -1):
    print(" ", end ="")
    #print(end="") #for left centered 
    #print(" " * i, end="") #for right centered
    print("*" * (n-i))