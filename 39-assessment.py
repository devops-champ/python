# st = 'Print only the words that start with s in this sentence'

# for word in st.split():
#     if word[0] == 's':
#         print(word)

# #2nd 

# my_list = range(0,11,2)

# print(list(my_list))

#3rd

# some_list = list(range(0,10))

# for divide in some_list:
#     if divide%3 == 0:
#         print(divide)
        
        
#4th

# dd = 'Print every word in this sentence that has an even number of letters'


# for i in dd.split():

#     if len(i)%2 ==0:
#         print(i, 'is even')
        
#5th


values = list(range(1,16))


for numbers in values:
    if numbers%3==0 and numbers%5==0:
        print(f'{numbers} is FizzBuzz')
    elif numbers%5==0:
        print(f'{numbers} is Buzz')
    elif numbers%3==0 and numbers%5==0:
        print(f'{numbers} is Fizz')
    
    



