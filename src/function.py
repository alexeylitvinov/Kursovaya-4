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


def get_validation_salary(text: int) -> int:
    """
    Если не указано поле в запросе вместо None возвращает текст 'Не указано'
    :param text: str
    :return: str
    """
    if text is None:
        text = 0
        return text
    return text


def get_main_menu():
    print('1 - Нажмите для поиска вакансий ')
    print('0 - Нажмите для для выхода из программы ')


def get_main_menu_second():
    print('Есть сохраненные результаты предыдущего поиска')
    print('2 - Нажмите для загрузки сохраненных данных из файла')
    print('3 - Очистить предыдущие результаты поиска')


def get_key_worlds_for_find():
    while True:
        user_input = input('Введите ключевые слова для поиска вакансий: ')
        if user_input.isdigit() or user_input is None:
            print('Не верно введено ключевое слово...')
        else:
            job_name = user_input
            break
    while True:
        user_input = input('Введите предполагаемую зарплату : ')
        if user_input.isnumeric() is False or user_input is None or int(user_input) <= 0:
            print('На ввод доступны только числа...')
        else:
            salary = int(user_input)
            break
    while True:
        user_input = input('Введите сколько вакансий показать: ')
        if user_input.isnumeric() is False or user_input is None or int(user_input) > 100 or int(user_input) <= 0:
            print('На ввод доступны только числа. Максимальное значение 100..')
        else:
            number_vacancies = int(user_input)
            break
    return job_name, salary, number_vacancies


def save_to_file(data, path_file):
    """
    Запись данных в .json файл
    :param data: json
    :param path_to_file: data, str
    :return: file.json
    """
    with open(path_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_to_file(path_to_file) -> json:
    """
    Загрузка данных из .json файла
    :param path_to_file: str
    :return: json
    """
    with open(path_to_file, encoding='utf-8') as file:
        data = json.load(file)
    return data


def delete_from_file(path_to_file):
    file = open(path_to_file, 'w')
    file.close()
