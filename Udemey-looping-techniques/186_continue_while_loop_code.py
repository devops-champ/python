

#write a code to check if a number is prime or not

import math


def find_divisors(num):
    '''
    this function will find all the divisors of a number
    '''
    divisors_list = [1, num] #start a list with the number 1
   
    
    divisor = 2 #start testing different divisors starting from the number 2
    
    
    while divisor <= math.sqrt(num):
            if num % divisor == 0:  #if the reminder is zero, it is evenly divisible by the divisor ie it is the divisor of the number
                divisors_list.append(divisor)
                divisors_list.append(num // divisor)
            divisor += 1
            
            
    return sorted(list(set(divisors_list))) 




while True:
    print("Enter a positive integer to check if it's prime number. Enter 's' to stop")
    
    value = input()
    
    
    if value == 's':
        break
    
    if (not value.isnumeric()) or (int(value)) <= 0:
        continue
    
    divisors = find_divisors(int(value))
    if len(divisors) == 2:
        print(f"This number {value} is prime")
    else:
        print(f"The number {value} is not prime")
        print(f"Divisors: {divisors}")          
                
                