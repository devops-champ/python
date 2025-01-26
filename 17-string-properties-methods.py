#concatenation

name = "sam"

letters = name[1:]


print('p' + letters)

#few more concatenation examples

x="hello world"

x= x + " it is beautiful outside"

print(x)


#multiplication with concatenation

word = "z"

print(word * 10)

#unexpected results when you try to concatenate a string.
a= '2' + '3'

print(a) #gives 23 instead of 5

#using attributes and methods aviaible in python (built-in)

y= "Hello friends"

print(y.upper(), y.lower())

#split method wihtout arguments splits based on whitesapce
print(y.split())

#split method with arguments splits based on the value and may include whitspace as well
d= "Hi this is a string"

print(d.split('i'))

#join method
z= [
    'a',
    'b',
    'c'
]
print(''.join(z)) 

#The join method is a string method in Python, which means it needs to be called on a string object,
# not a list object. When you try to call z. join(), Python will raise an AttributeError because join
# is not a method that can be used on lists. The correct usage is to call join() on a string, and pass the
# list as an argument. The string on which join() is called is used as a separator between the elements of the list.
