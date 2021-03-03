# Sample Input: 
# 4
# bcdef
# abcdef
# bcde
# bcdef

# Sample Output:
# 3
# 2 1 1

# Input format:
# The first line contains the integer n
# the next n lines each conatin a word

# Output format:
# Output two lines
# On the first line, output the number of distinct words from the input
# On the second line, output the number of occurencces of each distinct word according to their appearance in the input


input_value = int(input("Enter number: "))

list_of_input = []
for index in range(input_value):
    input_text = input("Enter text: ")
    list_of_input.append(input_text.lower())

count = {}
for index in range(len(list_of_input)):
    count_distinct = list_of_input.count(list_of_input[index])
    count[list_of_input[index]] = count_distinct
    
number_distinct_word = len(count)
print(number_distinct_word)

for key in count:
    print(count[key], end=" ")