# extract all the palindromes from a list and create a list with only palindromes


words = ["Vehicle", "Noon", "Kayak", "Child", "Anna", "Mother", "May"]
palindrome = []


def is_palindrome(letter):
    return letter == letter[::-1]


for letter in words:
    if is_palindrome(letter.lower()):
        palindrome.append(letter) 
        
        
print(palindrome)        
             