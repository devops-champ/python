

for i in range(4, 15, 2):
    for j in range(6, 17, 3):
        print(i + j)
        continue


print("=========space========") 
  
my_words = ["Python", "Loops", "While", "For", "Break", "Continue"]


for letters in my_words:
    if "e" in letters:
        continue
    print(letters.lower())
    
print("=========space========") 


i = 6

while i < 10:
    i += 2
    j = 2
    while j <= 5:
        print(i, j)
        j += 1
        if j < 4:
            continue
    
    
print("=========space========")

k = 5
 
while k < 16:
    print(k)
    while k == 5:
        continue
    k += 1
   