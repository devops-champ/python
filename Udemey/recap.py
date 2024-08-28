

def even_check(number):
    return number % 2 == 0


print(even_check(14545))



#return true if any number in the list is even


def even_list(number_list: list[int]) -> bool:
    '''returns true if any number in the list is even'''
    
    even = []
    
    for num in number_list:
        if num % 2 == 0:            
            even.append(num) 
        # else:
        #     pass
    
    return even #not all the returns have to be indented together.    

print(even_list([1,3,8]))        







work_hours = [('Abby', 1000), ('Billy', 400), ('cassie', 800)]


def employee_of_the_month(work_hours) -> tuple:
    
    max_hrs = 0
    emp = ''
    
    for name, hours in work_hours:
        if hours > max_hrs:
            max_hrs = hours
            emp = name
        else:
            pass
        
        
    return(emp, max_hrs)



print(employee_of_the_month(work_hours))        