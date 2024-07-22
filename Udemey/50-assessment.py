def lesser_of_two_evens(a,b):
    

    
 
    
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)    

    
print(lesser_of_two_evens(10,2))



def animal_crackers(a):
    
    wordlist = a.split()
    return wordlist[0][0]== wordlist[1][0]
        


print(animal_crackers('Level Zine'))