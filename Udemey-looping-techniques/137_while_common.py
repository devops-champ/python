#user input


valid_input = False #flag variable to control the while loop

while not valid_input:
    user_input = input("Please enter a number: ")
    
    if user_input.isnumeric():
        valid_input = True
    else:
        print("Please enter a valid input")   
        
        
        
auth = False #flag variable to control the while loop


while not auth:
    username = input("Enter Username")
    password = input("Enter password")
    
    if username == "admin" and password == "pass":
        auth = True
        print("Login into Prism success")
    else:
        print("Invaid username or password")
        
        
# read lines from a file until the end is reached

end_of_file = False

with open("example.txt", "r") as file:
    while not end_of_file:
        line = file.readline()
        
        if line == "":
            end_of_file = True
        else:
            print(line.strip())  

               