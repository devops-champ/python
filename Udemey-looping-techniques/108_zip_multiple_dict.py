first_dict = {"A": 10, "B": 25, "C": 13}
second_dict = {"A": 12, "B": 45, "C": 89}


for (key1, val1), (key2, val2) in zip(first_dict.items(), second_dict.items()):
    print(key1, val1, " / ", key2, val2)
    
    
for val1, val2 in zip(first_dict.values(), second_dict.values()):
    print(val1, "-", val2)    