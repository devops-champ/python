#validating user input using nested while loops

#ask the user to enter the students names and grades, and it will show the summary of all the grades.


grades = {}

continue_loop = True

while continue_loop:
    print("Enter the student name: ")
    is_valid = False
    
    while not is_valid:
        name = input()
        if name.isalpha():
            is_valid = True
        else:
            print("Enter a valid name")
            
            

    print("Enter the marks: ")
    is_valid = False                   
    
    while not is_valid:
        marks = input()
        if marks.isdigit() and (0 <= int(marks) <= 100):
            is_valid = True
        else:
            print("Enter a valid marks")
            
    grades[name] = marks   # to add entry to a dic, dictonary[key] = value


    print("Grade recorded. \n")
    print("Would you ask to enter the grade of another student")
    print("Enter 1 for 'yes' and 0 for 'no")

    is_valid = False

    while not is_valid:
        answer = int(input())
        if answer == 0:
            is_valid = True
            continue_loop = False
        elif answer == 1:
            is_valid = True
        else:
            print("Please enter a valid option")
            
    print()
    
    
print("----Final grades----")
for student, marks in grades.items():
    print(f"{student}: {marks}")                   
        
             