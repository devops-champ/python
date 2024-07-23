vowels = ["a", "e", "i", "o", "u"]

for i in range(len(vowels)):
    vowels[i] = vowels[i].upper()
    
print(vowels)


#using enmurate()

for index,char in enumerate(vowels):
    vowels[index]= vowels[index].upper()

print(vowels)      