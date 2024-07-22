# Reverse the casing of a string


my_string = "india"
reverse_case=""

for char in my_string:
    if char.isupper():
        reverse_case = reverse_case + char.lower()
    else:
        reverse_case = reverse_case + char.upper()
        
print(reverse_case)
              
              
#remove duplicates from a string

some_string = "aabbcc"
new_string = ""


for char in some_string:
    if char not in new_string:
        new_string += char
        
print(new_string)                