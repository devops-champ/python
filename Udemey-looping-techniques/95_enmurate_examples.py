# #iterate over the characters of a string and the counter starts at 5

# name = "Devops"

# for index, string in enumerate(name, 5):
#     print(index, string)
    
    
# # iterate over a tuple and we start the counter at 0   
# animals = ("Dog", "Cat", "Elephant", "Tiger")

# for index,values in enumerate(animals):
#     print(index, values)
    
    
# #iterate over the elements of a set and we start the counter at 1. Notice that the values are not processed in any specific order

# data = {5.6, 5.3, 5.8, 5.2, 5.7, 1.3, 7.3}

# for index,num in enumerate(data,1):
#     print(index, num)
    
    
pizzas = (["Margherita", 7.50], ["Vegetarian", 10.55], ["Meat Lovers", 8.45], ["Hawaiian", 8.3])



for index, (data, price) in enumerate(pizzas):
    pizzas[index][1] = round(15/100*price,2)
    
print(pizzas)


winners = [("William", 1530), ("Elizabeth", 1510), ("Frederick", 1500)]


for index,(name, points) in enumerate(winners, 1):
    print(index, "-", name, "with:", points, "points.")          