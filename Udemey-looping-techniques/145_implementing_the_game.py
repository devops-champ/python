low = 0
high = 1000


ans = (low + high) // 2


print("=======================================")
print("Welcome to the 'Guess  the Number' game")
print("=======================================")



print(f"Think of an integer between {low} and {high}...")


continue_loop = True
num_iterations = 0


while continue_loop:
    num_iterations += 1
    
    print(f"\n Is {ans} the number?")
    print("Enter 1 if the guess is too low")
    print("Enter 2 if the guess is too high")
    print("Enter 3 if the guess is correct")
    
    user_input = int(input("Answer: "))
    
    if user_input == 1:
        low = ans
    elif user_input == 2:
        high = ans
    elif user_input == 3:
        print(f"\n Found it! The number is: {ans}")
        if num_iterations == 1:
            print("It only took one iteration")
        else:
            print(f"It only took {num_iterations} iterations")
        continue_loop = False             
    else:
        print("Please enter a valid option")
        
    ans = (low + high) // 2 