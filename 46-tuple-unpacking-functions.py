
work_hours = [('Abby', 500), ('Billy', 300), ('Cesar', 400)]



def employee_check(work_hours):

    #placeholders
    current_max=0
    employee_of_month =''


    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
        
    #return
    return(employee_of_month, current_max)   


name,hour = employee_check(work_hours)
print(name)
#or 

print(employee_check(work_hours))