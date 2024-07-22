#continue goes to the top of the closest enclosing loop.

#used to skip the rest of the code inside the
#enclosing loop for the current iteration and move on to the next iteration of the loop.



my_string = "Darshan"

for letter in my_string:
    if letter == 'a':
        continue
    print(letter)
    
data = [1, None, 'hello', 42, 'world', None]

for item in data:
    if item == 'hello':
        continue
    print(item)
    
    
players = [{'name': 'Alice', 'active': True}, {'name': 'Bob', 'active': False}, {'name': 'Charlie', 'active': True}]


for player in players:
    if not player['active']:
        continue
    print(player)



