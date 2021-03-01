# pythonic way
from collections import Counter

input_value = int(input("Enter number: "))

list_of_input = []
for index in range(input_value):
    input_text = input("Enter text: ")
    list_of_input.append(input_text.lower())

count = Counter(list_of_input)
number_distinct_word = len(count)
print(number_distinct_word)

for key in count:
    print(count[key], end=" ")