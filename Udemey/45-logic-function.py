def even_check(number):
    return number % 2 == 0

print(even_check(13243))


#check even inside a list

def even_check_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
        
    return False
        
print(even_check_list([1,2,3]))
        

#retrun all the even numbers in a list

def even_num_list(even_list):
    
    #placeholders variables
    even_numbers=[]
    odd_numbers=[]
    
    for num in even_list:
        if num % 2 == 0:
            even_numbers.append(num)
        elif num %2 != 0:
            odd_numbers.append(num)    
        else:
            pass
        
    return even_numbers, odd_numbers      
        
print(even_num_list([100,9,8,47]))


#list comphresion
# def even_num_list_comp(even_list_comp):

#     even_numbers_list_comp=[num for num in even_list_comp if num % 2 == 0]
#     return even_numbers_list_comp

# print(even_num_list_comp([2,3,4]))

