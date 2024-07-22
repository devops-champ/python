numbers = [2, 3, 4, 5, 6]

for i in numbers:
    if i%2 == 0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd') 
        
        
#or

for i in range(len(numbers)):
    if numbers[i]%2 == 0:
        print(f'{numbers[i]} is even')
    else:
        print(f'{numbers[i]} is odd')
        
#enmurate()

for index, digits in enumerate(numbers):
    if numbers[index] % 2 == 0:
        print(f'{digits} is even')
    else:
        print(f'{digits} is odd')     
                  

word = "Manjula"

re_word = word[::-1]

if word == re_word:
    print(f'{word} is a pali')
else:
    print(f'{word} is NOT pali')                  