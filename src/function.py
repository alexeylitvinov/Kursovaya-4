import json


def delete_highlight(text: str):
    text = text.replace('<highlighttext>', '')
    text = text.replace('</highlighttext>', '')
    return text


def get_validation(text):
    if text is None:
        text = 'Не указано'
        return text
    return text


def load_from_file():
    with open('data/data_api.json', encoding='utf-8') as file:
        data = json.load(file)
    return data


def save_in_file(data):
    with open('data/data_api.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
