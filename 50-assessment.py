import sys
import time

def lesser_of_two_evens(a,b):
    
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    elif a % 2 != 0 or b % 2 != 0:
        
        return max(a,b)
    


print(lesser_of_two_evens(5,2))    
    

print("==============")
def animal_crackers(text):
    
        x = text.lower().split()
        
        first = x[0]
        second = x[1]
        
        return first[0] == second[0]
        
        #or 
        return x[0][0] == x[1][0]
    
print(animal_crackers('Levelheaded Klama'))   
    

print("==============")
def makes_twenty(n1,n2):
    
    return n1 + n2 == 20 or n1 == 20 or n2==20

    
print(makes_twenty(12,8))    
                    
                    
print("==============")

def old_macdonald(name):
        
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize() #slice the first three characters + slice from the fourth character
    else:
        return 'name is short'
    
print(old_macdonald('macdonald')) 


def master_yoda(text):   
    start_time = time.time()
    
    # Operation to measure
    result = ' '.join(text.split()[::-1])
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return result, execution_time

print(master_yoda('The following methods on bytes and bytearray objects can be used with arbitrary binary data.'))
    
                     
                     
def master_rada(text):
    start_time = time.time()
    
    x = text.split()
    y = " ".join(x[::-1])

    end_time = time.time()
    execution_time = end_time - start_time    
    
    return y, execution_time
                           
                           
print(master_rada('The following methods on bytes and bytearray objects can be used with arbitrary binary data.'))



#Given an integer n, return True if n is within 10 of either 100 or 200
print("==============")

def almost_there(n):
    return 90 <= n <= 110 or 190 <= n <= 210

    
print(almost_there(10)) 
                           

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
print("==============")

def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] ==3:
            return True
    return False


print(has_33([1, 3, 1])) 

#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

print("==============")

def paper_doll(text):
    value = ''
    
    for i in text:
        value += i * 3
    return value 

print(paper_doll('Hello'))


print("==============")
  
#Given three integers between 1 and 11, if their sum is less than or equal to 21, 
#return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
#Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'.


def blackjack(a,b,c):
    
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    if 11 in [a,b,c] and sum([a,b,c]) > 21:
        return sum([a,b,c])-10

    return 'BUST'
    

        
    
print(blackjack(9,9,11))



print("==============")

def summer_69(arr):
    count = 0
    
    for i in arr:
        if i is range(6,10):
            
            count += i
        
    return count  
 
    
print(summer_69([1,3,5])) 


#myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercas


print("==============")

def myfunc(text):
    skyline = ''
    
    for index,word in enumerate(text):
        
        if index % 2 == 0:
            skyline += word.lower()
        else:
            skyline += word.upper()    

            
    return skyline

print(myfunc('Darshan'))


print("==============")


def spy_game(nums):
    
    for i in range(len(nums)-1):
        if nums[i] ==0 and nums[i] == 7:
            return True
    return False


print(spy_game([1,2,4,0,0,7,5]))
        
                                    