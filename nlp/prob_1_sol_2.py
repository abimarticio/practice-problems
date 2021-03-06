import requests
from string import punctuation
from collections import Counter

def download_file():
    url = 'http://norvig.com/big.txt'
    r = requests.get(url, allow_redirects=True)
    open('big.txt', 'wb').write(r.content)
    with open('big.txt', 'r') as text_file:
        data = text_file.readlines()
    return data

def remove_punctuation_marks(data: list, punctuation: str) -> list:
    new_line = []
    for line in data:
        line = line.strip().translate(str.maketrans("\n\t", "  ", punctuation))
        if line != "":
            new_line.append(line)
    return new_line

def get_num_words(clean_file: list) -> list:
    list_of_words = []
    for line in clean_file:
        for word in line.split():
            if not word.isdigit():
                list_of_words.append(word.lower())
    return list_of_words
    
def get_unique_words(list_of_words: list) -> dict:
    unique = Counter(list_of_words)
    return unique

def ten_most_occuring_words(unique: dict):
    ten_most_unique_words = dict(sorted(unique.items(), key=lambda item: item[1], reverse=True)[:10])
    return ten_most_unique_words

def ten_least_occuring_words(unique: dict):
    ten_least_unique_words = dict(sorted(unique.items(), key=lambda item: item[1])[:10])
    return ten_least_unique_words

def main():
    load_data = download_file()
    my_punctuation = punctuation.replace("'", "")
    clean_file = remove_punctuation_marks(data=load_data, punctuation=my_punctuation)
    total_words = get_num_words(clean_file=clean_file)
    count_unique = get_unique_words(list_of_words=total_words)
    ten_most_words = ten_most_occuring_words(unique=count_unique) 
    ten_least_words = ten_least_occuring_words(unique=count_unique)
    total_num_words = (len(total_words))
    total_unique_words = (len(count_unique))
    print(f"Total number of words: {total_num_words}")
    print(f"Total number of unique words: {total_unique_words}")
    print(f"Top 10 most frequently occuring word: {ten_most_words}")
    print(f"Top 10 least frequently occuring word: {ten_least_words}")

main()