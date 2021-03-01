# Game rules:
# Both players are given the same string
# Both players have to make substrings using the letters of the string
# Stuart has to make words starting with consonants
# Kevin has to make words starting with vowels
# The game ends when both players have made all the possible substrings

# Scoring
# A player gets +1 point for each occurence of the substring

def vowel_beginning(word):
    vowel_list = []
    for index in range(len(word)):
        for i in range(len(word)):
            if word[index] in ('A', 'E', 'I', 'O', 'U'):
                new_word = word[index:i+1]
                if new_word != "":
                    vowel_list.append(new_word)

    vowel = {}
    for index in range(len(vowel_list)):
        count = vowel_list.count(vowel_list[index])
        vowel[vowel_list[index]] = count

    total = 0
    for value in vowel:
        total += vowel[value]
    return total


def consonant_beginning(word):
    cons_list = []
    for index in range(len(word)):
        for i in range(len(word)):
            if word[index] not in ('A', 'E', 'I', 'O', 'U'):
                new_word = word[index:i+1]
                if new_word != "":
                    cons_list.append(new_word)

    cons = {}
    for word in cons_list:
        count = cons_list.count(word)
        cons[word] = count

    total = 0
    for value in cons.values():
        total += value
    return total

def main():
    word = "BANANA"
    kevin_score = vowel_beginning(word=word)
    stuart_score = consonant_beginning(word=word)
    print(f"Kevin {kevin_score}")
    print(f"Stuart {stuart_score}")
main()