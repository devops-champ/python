category = ["red", "green", "blue"]
color = [235, 150, 2]


print(dict(zip(category, color)))



str1 = "aabbcccddee"
str2 = "aaabccddeee"


out=0
for word1, word2 in zip(str1, str2):
    if word1 in word2:
        out += 1
print(out) 


chars = ["*", "-", "#", "="]
repetitions = [5, 4, 3, 2]


for value, rep in zip(chars, repetitions):
    print(value*rep) 
    
    
listA = [(1, "A"), (2, "b"), (3, "C"), (4, "e")]
listB = [(1, "a"), (2, "b"), (3, "C"), (6, "f")]

for a, b in zip(listA, listB):
    if a == b:
        print("Equal")
    else:
        print("Not Equal")          