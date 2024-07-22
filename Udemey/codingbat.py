# def string_times(string, n):
#     result=''
    
#     for i in range(n):
#         result+=string
#     return result
    
#     # return string * n


# print(string_times('Hi',2))


def front_times(string, n):
    
    length=3
    
    if length > len(string):
        length = len(string)
    font = string[:length]    
    
    result=''
    
    for i in range(n):   
        result+=font
    return result

print(front_times('ab', 3))    

