chemical_elements = {
    "Hydrogen": "H",
    "Helium": "He",
    "Beryllium": "Be",
    "Boron": "B",
    "Carbon": "C",
    "Nitrogen": "N",
    "Oxygen": "O",
    "Fluorine": "F",
    "Neon": "Ne"
}

pizza_prices = {
    "Cheese Pizza": 11.99,
    "Pepperoni Pizza": 14.99,
    "BBQ Chicken Pizza": 13.99,
    "Hawaiian Pizza": 12.99,
    "Meat Pizza": 16.99
}

if "Pepperoni Pizza" in pizza_prices:
    pizza_prices["Pepperoni"] = pizza_prices["Pepperoni Pizza"]
    del pizza_prices["Pepperoni Pizza"]
print(pizza_prices)




for a,b in pizza_prices.items():
    pizza_prices[a] = round(b *1.15, 2)
print(pizza_prices)    


seq = (["A", "B", "C"], "Hello", ["D", "E", "F"], 5, ["G", "D", "E"])

target = "G"

        
for elem in seq:
    if isinstance(elem, list) and (target in elem):
        print("Found")
        
        
num = 10
print(isinstance(num, (int, str)))      