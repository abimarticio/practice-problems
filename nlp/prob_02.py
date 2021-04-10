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

def main():
    data = load_data(filename='avengers_endgame.txt')
    lines = list_lines(data=data)

main()