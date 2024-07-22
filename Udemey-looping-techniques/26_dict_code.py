dictionary = {"a": 45, "b": 60}

#add a key-pair value
dictionary["c"] = 100

print(dictionary)

#update key
dictionary["a"] = 50

print(dictionary)

#delete dict
del dictionary["c"]

print(dictionary)


grades = {
    "Nora": 86,
    "Gino": 55
    }

#get both key value pair

print(grades.items())

#update method

grades.update({"Nora": 26, "Jack": 19})

print(grades)