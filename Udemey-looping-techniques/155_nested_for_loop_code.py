# print a pattern of pyramid with 5 rows


num_rows = 5


#iteration  |    i    |   num_rows-i
#   1           1           5-1 =4
#   2           2           5-2 =3
#   3           3           5-3=2
#   4           4           5-4=1
#   5           5

for i in range(1, num_rows+1):
    
    #printing spaces
    for space in range(num_rows-i):
    #print(space)
        print(" ", end ="")
        
    #printing asterisks
    for ast in range(i):
        print("*", end= " ")
        
    print()    
    