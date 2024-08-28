import pprint
# stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
# stuff.insert(0, stuff)
# pprint.pp(stuff)


letters_freq = {}


with open("Metamorphosis+by+Franz+Kafka.txt", "r") as file:
    for line in file:
        for word in line.split():
            for char in word:
                if char.isalpha(): #check if the character is alphabetical
                    if char.lower() in letters_freq: #check if the lowercase version of that character is already in the dic
                        letters_freq[char.lower()] += 1   #if the character is already in the dictionary, then increment the instaces of that character
                    else:
                        letters_freq[char.lower()] = 1   #if the character is not in the dictionary, then add it to the dic
                    
                    
print(f"Most frequent letter: {max(letters_freq, key=letters_freq.get)}")
print(f"Frequency:")
pprint.pprint(letters_freq)                       