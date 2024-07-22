#generate sequence at the start of index 1,
#and it will end at the length of the word.
#sequence of 2

word = "All is well"

for i in range(1, len(word), 2):
    print(word[i])
    
    
#find all the odd numbers upto 50

n = 50
odd_numbers = []

for num in range(1, n, 2):
    odd_numbers.append(num)
    
    
print(odd_numbers)   