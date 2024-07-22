word = "earth"

vowels = []

for i in range(len(word)):
    if word[i] in "aeiou":
         vowels.append(i)
    # elif word[i] == "e":
    #     vowels.append(i)    
    # elif word[i] == "i":
    #     vowels.append(i)
    # elif word[i] == "o":
    #     vowels.append(i) 
    # elif word[i] == "u":
    #     vowels.append(i)                     
        
print(f'Number of vowels in {word}: {len(vowels)}')  


#or

# def count_vowels(word):
#     vowels = "aeiou"
#     counter = 0
#     for i in range(len(word)):
#         if word[i] in vowels:
#             counter += 1
#     print(f"Number of vowels in {word}: {counter}")

# count_vowels("Darshan")    