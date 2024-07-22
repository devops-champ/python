my_tuples = [("a", 5), ("b", 8,), ("c", 0,), ("d", 20)]

def get_last_elem(value):
    return value[-1]

for char, num in sorted(my_tuples, key=get_last_elem):
    print(char, num)
    
    
some_tuple = (1, 10, 6, 4)

print(sorted(some_tuple))    