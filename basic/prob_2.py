# Create a dictionary that uses the index number of the element as the key,
# e.g. if we have the following array, names = [“Ana”, “Ben”, “Carl”, “Dana”],
# its dictionary equivalent should be {0: “Ana”, 1: “Ben”, 2: “Carl”, 3: “Dana”}.
# Show each and every solution you can think of as there could be more than one.

names = ["Anna", "Ben", "Carl", "Dana"]

names_dict = {}

# solution_1
# for loop
# for index in range(len(names)):
#     names_dict[index] = names[index]
# print(names_dict)

# solution_2
# while loop
# index = 0
# while(index < len(names)):
#     names_dict[index] = names[index]
#     index +=1
# print(names_dict)

# solution_3
for key, value in enumerate(names):
    names_dict[key] = value
print(names_dict)