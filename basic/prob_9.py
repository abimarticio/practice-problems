# input: 1a2b3c
# output: abbccc

user_input = "1a2b3c"

list_num = []
list_char = []
for index in range(len(user_input)):
    value = user_input[index]
    if value.isnumeric():
        value = int(value)
        list_num.append(value)
        
    else:
        list_char.append(value)

output = ""
for index in range(len(list_num)):
    output += (list_num[index] * list_char[index])

print(output)