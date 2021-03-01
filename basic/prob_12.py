# Get the Hamming distance.
# Hamming distance is the number of positions at which the corresponding symbols in compared strings are different.
# Input
# KAROLIN
# KERSTIN
# Output
# 3

def get_hamming_distance(first_text: str, second_text: str):
    count = 0
    for index in range(len(first_text)):
        if first_text[index] != second_text[index]:
            count += 1
    return count

def main():
    first_text = input("Enter text: ")
    second_text = input("Enter text: ")
    if len(first_text.upper()) == len(second_text.upper()):
        hamming_distance = get_hamming_distance(first_text=first_text, second_text=second_text)
        print(hamming_distance)
    else:
        print("Not equal in length!")

main()