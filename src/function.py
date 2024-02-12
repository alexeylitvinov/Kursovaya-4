import json


def delete_highlight(text: str) -> str:
    """
    Удаляет из текста <highlighttext> </highlighttext> строки
    :param text: str
    :return: str
    """
    text = text.replace('<highlighttext>', '')
    text = text.replace('</highlighttext>', '')
    return text


def get_validation(text: str) -> str:
    """
    Если не указано поле в запросе вместо None возвращает текст 'Не указано'
    :param text: str
    :return: str
    """
    if text is None:
        text = 'Не указано'
        return text
    return text


def load_from_file(path_to_file: str) -> json:
    """
    Загрузка данных из .json файла
    :param path_to_file: str
    :return: json
    """
    with open(path_to_file, encoding='utf-8') as file:
        data = json.load(file)
    return data


def save_in_file(data: json, path_to_file: str):
    """
    Запись данных в .json файл
    :param data: json
    :param path_to_file: data, str
    :return: file.json
    """
    with open(path_to_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def get_main_menu():
    print('1 - Нажмите для поиска вакансий ')
    print('0 - Нажмите для для выхода из программы ')


def get_main_menu_second():
    print('Есть сохраненные результаты предыдущего поиска')
    print('2 - Нажмите для загрузки сохраненных данных из файла')


def get_key_worlds_menu_for_find():
    job_name = input('Введите ключевые слова для поиска вакансий: ')
    salary = input('Введите предполагаемую зарплату : ')
    number_vacancies = input('Введите сколько вакансий показать: ')
    return job_name, salary, number_vacancies
