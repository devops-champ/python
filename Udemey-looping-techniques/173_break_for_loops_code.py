

#validate a user input. ask user to enter 0, 1, 2. if any value other than 0, 1, 2. it should say enter valid number


#print("Enter any number: 0, 1, or 2")

is_valid =  False

while not is_valid:
    values = input("Enter any number: 0, 1, or 2: \n")
    if values in ['0', '1', '2']:
        is_valid = True
        print(f"You entered {int(values)}")
    