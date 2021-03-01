# pythonic way
from collections import Counter

user_input = "aabbbccde"
user_input = list(user_input)
count = Counter(user_input)
sorted_dict = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))

for key in list(sorted_dict)[:3]:
    print(key, sorted_dict[key])