# input format: aabbbccde
# output format: b 3
#                a 2
#                c 2
# print three most common characters along with their occurrence count each on a separate line
# sort output in descending order of occurrence count
# if the occurrence count is the same, sort the characters in alphabetical order

import operator
user_input = "aabbbccde"
user_input = sorted(user_input)
input_dict = {}
for index in range(len(user_input)):
    count = user_input.count(user_input[index])
    input_dict[user_input[index]] = count

sorted_dict = dict(sorted(input_dict.items(), key=operator.itemgetter(1),reverse=True))

for key in list(sorted_dict)[:3]:
    print(key, sorted_dict[key])