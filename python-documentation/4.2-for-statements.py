

words = ['cat', 'window', 'defenestrate']


for index, items in enumerate(words):
    print(items, len(items))
    
# Create a sample collection    
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}


# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
        
active_users = {}

for user, status in users.items():
    if status == 'active':
        active_users[user] = status
        
print(users)
print(active_users)                 



