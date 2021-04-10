def load_data(filename: str) -> list:
    with open(filename, 'r', encoding='utf-8') as text_file:
        data = text_file.readlines()
    return data