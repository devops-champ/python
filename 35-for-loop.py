sample_list = [1,2,3]

sum_total = 0

for ran in sample_list:
    sum_total += ran
print(ran)  #output is 3 becuase ran is set to the current no of each loop, its value is the last number in the loop
    
for value in sample_list:
    if value % 2 == 0:
        print(str(value) + " even")
    elif value % 2 != 0:
        print((str(value) + " odd"))  


string_value = "Darshan"
reverse_s = ''

for i in string_value:
    reverse_s = i + reverse_s
print(reverse_s)     


#variable initalization or running tally

num = 0

for init in sample_list:
    num += init
print(num)

#iterate without using a variable

for _ in "Hello":
    print("Hello")

   
#dictionaries    
d = {
    'k1': 1,
    'k2': 2,
    'k3': 3
}

for i in d.items():
    print(i)


#unpacking tuples

students = [("John", 85), ("Jane", 90), ("Bob", 78)]


for name,marks in students:
    print(marks)
    
    
tlist = [(1,2),(3,4),(5,6)]


for a,b in tlist:
    print(b)   