programming_languages = ["Python", "Javascript", "C++"]

# print(len(programming_languages[1]))

#pick range of indeces from the list

print(programming_languages[0:2])

#reverse the list

# a=programming_languages[::-1]

# reversed_strings = [s[::-1] for s in a]
# print(reversed_strings)

# programming_languages.reverse()

for i in range(len(programming_languages)): 
    programming_languages[i] = programming_languages[i][::-1]
    
programming_languages.reverse()
print(programming_languages)    
   

# reverse_s = []
# for i in programming_languages:
#     reverse_s.append(i[::-1])

# reverse_s.reverse()
# print(reverse_s)


#list methods

#append
programming_languages.append("C#")


#extend
more_languages = ["Go", "Ruby"]
programming_languages.extend(more_languages)

# #insert string at a particluar index
programming_languages.insert(0, "Java")

# #remove
programming_languages.remove("Python")


# #sort
programming_languages.sort()

# #reverse
programming_languages.reverse()

# #pop
programming_languages.pop(0)

#clear
programming_languages.clear()

#index
programming_languages.index("C++")
print(programming_languages)