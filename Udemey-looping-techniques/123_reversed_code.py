my_list = [1, 3, 5, 6, 7]

print(list(reversed(my_list)))

print("------place holder-------")
my_kv = {
    "Z": 5,
    "A": 10,
    "C": 15,
    "M": 6
}

print(list(reversed(my_kv.items())))

print("------place holder-------")
students = ("Gino", "Nora", "Talina", "Fanny", "Loretto", "Eric")

for names in sorted(students, key= lambda x: x.capitalize()):
    print(names)
    
print("------place holder-------")    
numbers = [5, 15, 7, 4, 8, 12, 9, 3]

count = 0

for values in reversed(numbers):
    if values %2 == 0:
        count += values
        
print(sum)

print("------place holder-------")

posts = {
    "2354": {
        "user": "Python51",
        "content": "I really like this",
        "likes": 35
    },
    "2355": {
        "user": "Loops55",
        "content": "Awesome",
        "likes": 123
    },
    "2356": {
        "user": "Coder58",
        "content": "This is really good",
        "likes": 27
    }
}


def get_likes(post):
    return post["likes"]


def display_sorted_posts(posts):
    for post in sorted(posts.values(), key=get_likes, reverse=True):
        print(post["content"])

        
display_sorted_posts(posts)                    