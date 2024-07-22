#print all the substrings of length 2 excluding the first and last characters.

word = "Darshan"


for i in range(1, len(word)-2):
    print(word[i:i+2])
    #or
    print(word[i])