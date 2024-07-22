my_dict = {
    "a": 15,
    "b": 20,
    "c": 30
}

for count, value in enumerate(my_dict.items()):
    print("count:", count, "-value", value)
    
    
#multiple variables
for count, (key, value) in enumerate(my_dict.items()):
    print("count:", count, "-key:", key, "-value", value)   
    