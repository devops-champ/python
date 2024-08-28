

#this program will take user input string and letter and checks if the letter is part of the string


print("Let's find if a letter is present in the string")

text = input("Enter the string: ")
letter = input("Enter the letter: ")


for char in text:
    print(char)
    if char == letter:
        print("Found it")
        break