# dictionaries are unordered and cannot be sorted


my_dict = {
    'k1': 'python',
    'k2': 'rust',
    'k3': 'golang'
}

print(my_dict['k2'])

#holding lists and other dictonaries
some_dict = {
    'q1': 1234,
    'q2': [
        'blue',
        'green',
        'yellow',
        'orange'
    ],
    'q3': {
        'a1': 'mountain',
        'a2': 'rivers',
        'a3': 'beach'
    }
}

#print(some_dict['q2'][2])

print(some_dict['q3']['a2'].upper())

#Updating the dict

h1_01 = {
    'h1': 100,
    'h2': 200
}

h1_01['h3'] = 300

print(h1_01)

#over-write existing key-vale pair

h1_01['h2'] = 500

print(h1_01)

print(h1_01.keys()) #only keys

print(h1_01.values()) #only values

print(h1_01.items()) #key-value pairs as tuples