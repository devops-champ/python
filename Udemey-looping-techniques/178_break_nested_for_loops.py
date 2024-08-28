

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]


for seq in my_list:
    
    for elem in seq:
        
        if elem > 5:           
            print("Found it")
            break
        
'''
- **Second Iteration (Outer Loop)**:
  - `seq = [4, 5, 6]`
  - **Inner Loop**:
    - `elem = 4` (condition `elem > 5` is `False`)
    - `elem = 5` (condition `elem > 5` is `False`)
    - `elem = 6` (condition `elem > 5` is `True`)
      - Prints "Found it"
      - Executes `break`, exits inner loop.

- **Third Iteration (Outer Loop)**:
  - `seq = [7, 8, 9]`
  - **Inner Loop**:
    - `elem = 7` (condition `elem > 5` is `True`)
      - Prints "Found it"
      - Executes `break`, exits inner loop.
'''        



for i in range(1500):
    for j in range(30):
        print("Hello")
        break
    
    break