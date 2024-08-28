a = ["bb", "ddd", "z"]

print(sorted(a, key=len))


for elem in sorted(a, key=len):
    print(elem)
    

print("=======================")
#using custom function
    
k1 = ["bc", "dda", "cd"]

# criteria:
# function must take:
# --> one parameter
# --> based on parameter, return a value
# --> value will be used in sorted method



def rev_string(string):
    return string[-1]


for char in sorted(k1, key=rev_string):
    print(char)    