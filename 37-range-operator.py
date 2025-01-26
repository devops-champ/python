# for i in range(2):
#     print(i)
    
    
# some_range = range(4)
# print(list(some_range))


# index_count =0

# for letter in 'abcde':
#     index_count += 1
#     print(f'At index {index_count} the letter is {letter}')
    
    
word = 'abcde'

for index,letters in enumerate(word):
    
    print(letters)
    print('\n')
    print(index)
    
# value = list()

# print(value)

a = ['Mary', 'had', 'a', 'little', 'lamb']

for a,b in enumerate(a):
    #when i=0, then a[i] is a[0] which is Mary
    print(a,b)

