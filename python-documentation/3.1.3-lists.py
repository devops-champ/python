#Lists also support operations like concatenation

squares = [1, 4, 9, 16, 25]

print(squares + [36, 49, 64, 81, 100])


#add new items at the end of the list, by using the list.append() method 
cubes = [1, 8, 27, 65, 125]

cubes.append(216)
print(cubes)


#reassigning the list to new variables still points to the original variable
rgb = ["Red", "Green", "Blue"]
a = rgb

a.append("Alpha")

print(rgb)

corrected_a = a[:]  #created a copy of the list. No start and no stop.

print(corrected_a)

corrected_a[-1] = "Zozo"

print(corrected_a)


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
'''
            0    1    2    3    4    5    6
'''

letters[2:5] = ['C', 'D', 'E']
print(letters)

letters[2:5] = []
print(letters)


# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)


a = ['a', 'b', 'c']
n = [1, 2, 3]

x = [a, n]

print(x[0])
print(x[0][1])