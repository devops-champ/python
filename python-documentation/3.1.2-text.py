s = 'First line.\nSecond line.'
print(s)


#use raw strings by adding an r before the first quote:

print(r'\Users\darshan')


#string literals can span multiple lines by using '''...''' or """...""" 
#End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line.
print("""\
Usuage: thingy options
    -h              display this use
    -H              hostname to connect to \
""")

#strings concatenation

print(3 * 'un' + 'ium')

#Two or more string literals next to each other are automatically concatenated.
#this doesn't work with expressions and variables
#print('py' 'thon')


prefix = 'py'
print(prefix + 'thon')


#Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error
word = 'Devops'


print('J' + word[:-1])
