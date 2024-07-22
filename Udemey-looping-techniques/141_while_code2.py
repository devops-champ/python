cont_loop = True


while cont_loop:
    print("Do you like to add two numbers?")
    ans = input("Please enter 'yes' or 'no': ")
    
    if ans == "yes":
        
        num1 = int(input("Enter your first number:  "))
        num2 = int(input("Enter your second number:  "))
        total = num1 + num2
    
        print(f'Total of {num1} and {num2} is {total}')
        
    elif ans == "no":
        cont_loop = False 
        
        
set_loop = True

while set_loop:
    print("Please enter two numbers")
    nu1 = int(input())
    nu2 = int(input())  
    print(f'{nu1} + {nu2} = {nu1 + nu2}')
    
    print("Would you like to enter two new integers?")
    ans = input("Please enter 'yes' or 'no': ")
    
    
    if ans == "no":
        set_loop = False
                