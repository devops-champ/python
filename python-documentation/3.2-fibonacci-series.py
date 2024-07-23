"""
The Fibonacci sequence is a series of numbers

  where each number is the sum of the two preceding ones,

  usually starting with 0 and 1.
"""

#it's an example of tuple unpacking in python

a, b = 0, 1

while a < 1000:
    print(a, end=', ')
    a, b = b , a+b
    
    
    
"""
iteration   a   b   printa     a=b, b=a+b
    1       0   1     0         1,  1
"""    