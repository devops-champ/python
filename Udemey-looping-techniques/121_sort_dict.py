distances = {
    "A": 342,
    "B": 653,
    "C": 231,
    "D": 684,
    "E": 1232,
    "F": 214
}

for city in sorted(distances, reverse=True):
    print(city)
    
    
for city, val in sorted(distances.items()):
    print(city, val)
    
print("end")    
#custom function using lambda functions

for city, val in sorted(distances.items(), key=lambda x: x[1]):
    print(city, val)


print("end")
# reverse with custom function using lambda functions 

for city, val in sorted(distances.items(), key=lambda x: x[1], reverse=True):
    print(city, val)       