#multiply the numbers at odd indices by 2

num_list = [1, 10, 20, 30, 40, 50]


for index, num in enumerate(num_list):
    if index % 2 != 0:
        num_list[index]= num * 2
        
print(num_list)       