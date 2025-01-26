#.format method

#syntax
#string {}.format('something')

print("This is a string {}".format('awesome'))

#based on index position
print("The {} {} {}".format('brown', 'fox', 'trick'))

print("The {1} {0} {2}".format('brown', 'fox', 'trick'))

#based on keywords

print("The {t} {b} {f}".format(b='brown', f='fox', t='trick'))



#float formatting with .format

#{value:width.precision f}

result = 100/777

print("The result was {:1.5f}".format(result))

data = {
    'b': 'brown',
    'f': 'fox', 
    't': 'trick'
    }

print("{b}".format(**data)) #** is used to unpack dictionary
#or
print(f'{data['b']}')


ldata = ['brown', 'fox', 'trick']
print("The {2}".format(*ldata)) #* is used to unpack a list



#f-strings method (formatted string literals)

name = "josh"

print(f"His name is {name}")

#float formatting with f-string

#{value:{width}:{precision}}

discount = 23.45684

print(f'The discount is {discount:20.1f}') 