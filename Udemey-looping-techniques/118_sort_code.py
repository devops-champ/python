#sorted returns a new list containing all items from the iterable in ascending order.


l1_list = [2, 1, 0, 8, 3]

t1_list = (10, 30, 50, 40)

print(sorted(l1_list))

print(sorted(t1_list, reverse=True))


my_dict = {
    "a": 20,
    "z": 30,
    "g": 60,
    "d": 40,
    
}

print(sorted(my_dict.values()))
print(sorted(my_dict.items()))


word = "Darshan"

print(sorted(word))