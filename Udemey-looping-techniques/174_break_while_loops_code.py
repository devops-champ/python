
data = []

print("Enter the data")
print("Enter -1 to stop")

while True: # use True or False to intentionally make the loop infinite
    num = int(input("Value: "))
    if num == -1:
        break
    data.append(num)


print(data)    