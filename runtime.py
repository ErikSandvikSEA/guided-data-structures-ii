command = input

# if command in ['n', 's', 'e', 'w'] 

commands = ['n', 's', 'e', 'w', ... 1000] 

# ================================================ CONSTANTS ======================================== 
commands[1] # constant time operation, because it doesn't matter how large the input is, we can always grab the [1] index in the same amount of time

# accessing a dictionary value by key 

rooms = {"outside": Room(...), ... }
rooms["outside"] # similar story as accessing a list element by index. Doesn't matter how big the input is, because we can still grab the 'outside' key's value by referencing it directly

# ================================================ LINEARS ======================================== 
# linear time -- depends on number of elements in the commands list 
for command in commands:
    #do something
    # adding 1 to list size increases number of loope iterations by c for input by 1

for key, value in rooms.items(): # linear time

# ================================================ QUADRATIC ======================================== 
# print out every combination of pairs of commands in our commands list 
# for every additional input, it grows O(n^2)
for i in commands:
    for j in comands:
        print(x, y)



# runtime complexity 