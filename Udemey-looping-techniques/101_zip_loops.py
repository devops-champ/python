a = [1, 2, 3, 4]
b = [1, 2, 3, 5]


are_equal = True

for num1, num2 in zip(a,b):
    if num1 != num2:
        are_equal = False
        
print(are_equal)       


#If you pass one argument to zip(), the sequence will have tuples of length 1
my_list = [1, 2, 3, 4]

print(list(zip(my_list))) 


lang = ["Python", "Go", "Groovy", "Javascript"]

for index, words in enumerate(lang):
    lang[index] = lang[index][::-1]
    
print(lang)    