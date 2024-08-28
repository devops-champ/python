

for i in range(2,4):
    for j in range(2):
        if (i+j) % 2 == 0:
            continue
        print(i,j)
        
        
print("=======space========")        
i =0

while i < 2:
    j = 0
    while j < 3:
        j += 1
        if j % 2 == 0:
            continue
        print(i, j)
    
    i += 1          