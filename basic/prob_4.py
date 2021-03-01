# Display the first two names only from the names list. 
# Show as many solutions as you can think.
# names = [“Ana”, “Ben”, “Carl”, “Dana”]

names = ["Anna", "Ben", "Carl", "Dana"]

print(names[:2])

# solution_1
index = 0
while(index < 2):
    print(names[index])
    index += 1

# solution_2
for index in range(0, 2):
    print(names[index])

#solution_3
for index, name in enumerate(names):
    if index < 2:
        print(name)