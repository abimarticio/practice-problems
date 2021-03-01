from collections import Counter

def vowel_beginning(word):
    vowel_list = []
    for index in range(len(word)):
        for i in range(len(word)):
            if word[index] in ('A', 'E', 'I', 'O', 'U'):
                new_word = word[index:i+1]
                if new_word != "":
                    vowel_list.append(new_word)

    vowel = Counter(vowel_list)
    total = sum(vowel.values())
    return total

def consonant_beginning(word):
    cons_list = []
    for index in range(len(word)):
        for i in range(len(word)):
            if word[index] not in ('A', 'E', 'I', 'O', 'U'):
                new_word = word[index:i+1]
                if new_word != "":
                    cons_list.append(new_word)

    cons = Counter(cons_list)
    total = sum(cons.values())
    return total

def main():
    word = "BANANA"
    kevin = vowel_beginning(word=word)
    stuart = consonant_beginning(word=word)
    print(kevin)
    print(stuart)
main()
