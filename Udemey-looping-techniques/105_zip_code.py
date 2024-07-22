a = [1, 2, 3]
b = [2, 4, 5]
c = [5, 8, 9]

print(list(zip(a, b, c)))

for num1, num2, num3 in zip(a, b, c):
    print(num2)


k1 = [1, 2, 3]
k2 = [4, 5]
k3 = [6, 7, 8, 9]

print(list(zip(k1, k2, k3)))    