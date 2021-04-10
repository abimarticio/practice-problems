import re

def load_data(filename: str) -> list:
    with open(filename, 'r', encoding='utf-8') as text_file:
        data = text_file.readlines()
    return data

def list_lines(data: list):
    lines = []
    for line in data:
        line = line.strip('\n')
        if ':' in line:
            line = re.sub(r"[^a-zA-Z0-9:'[\](\)]+", " ", line)
            line = re.sub(r'\[.*?\]', '', line)
            line = re.sub(r'(?:^|\W)English(?:$|\W)\)|(?:^|\W)Translated(?:$|\W)|\((.*?)\)|(\))', '', line)
            line = line.strip()
            if line != "":
                lines.append(line)
    return lines

def get_dict_lines(lines: list):
    dict_lines = {}
    for line in lines:
        new_line = line.split(':')
        key = new_line[0].strip()
        value = new_line[1].strip()
        if key not in dict_lines:
            dict_lines[key] = []
        dict_lines[key].append(value)
    return dict_lines

def get_num_of_words(lines: list):
    list_words = []
    for line in lines:
        line = line.split(':')
        line = line[1].split()
        for word in line:
            list_words.append(word.lower())
    return list_words



def main():
    data = load_data(filename='avengers_endgame.txt')
    lines = list_lines(data=data)
    dict_lines = get_dict_lines(lines=lines)
    num_of_words = get_num_of_words(lines=lines)
    total_num_words = len(num_of_words)
    print(f'Total number of words: {total_num_words}')

main()