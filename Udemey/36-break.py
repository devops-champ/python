#break used to exit or "break" out of a loop before it has finished iterating over
# all items. Once a `break` statement is encountered, the program's control flow 
# immediately exits the loop and continues with the next statement after the loop.

my_string = 'Devops'

for letter in my_string:
    if letter == 'e':
        break
    print(letter)