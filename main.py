import os

from src.from_api import HHRuApi
from src.function import load_from_file, get_main_menu, get_main_menu_second, get_key_worlds_menu_for_find, save_in_file
from src.vacancies import Vacancies

job_name = ''
salary = ''
number_vacancies = ''
path_data_file = 'data/data_api.json'


def user_interface():
    """
    Функция для взаимодействия с пользователем
    :return: None
    """
    global job_name
    global salary
    global number_vacancies
    hh_ru = HHRuApi()
    vacancies = None
    save_list = []
    print('Привет! Займемся поиском вакансий на HH.ru ')
    print('=' * 100)
    while True:
        get_main_menu()
        if os.path.getsize(path_data_file) != 0:
            get_main_menu_second()
        command = input('Введите команду: ')
        if command == '1':
            Vacancies.list_vacancies = []
            print('=' * 100)
            try:
                data = hh_ru.get_vacancies(*get_key_worlds_menu_for_find())
                for i in data['items']:
                    vacancies = Vacancies(i)
            except KeyError:
                print('Не все поля запросов были заполнены или заполнены не корректно')
            try:
                for i in vacancies.list_vacancies:
                    i.get_print_class_field()
                    print('=' * 100)
            except:
                print('По таким критериям ничего не найдено')
            answer = input('Сохранить найденные данные в файл? Нажмите "s" чтобы сохранить, чтобы продолжить нажмите '
                           'любую клавишу:   ')
            if answer == 'ы' or answer == 's':
                for i in vacancies.list_vacancies:
                    save_list.append(i.__dict__)
                save_in_file(save_list, path_data_file)
        elif command == '2':
            Vacancies.list_vacancies = []
            data_api = load_from_file(path_data_file)
            for i in data_api:
                vacancies = Vacancies(i)
            for i in vacancies.list_vacancies:
                i.get_print_class_field()
                print('=' * 100)
        elif command == '0':
            print('Всего хорошего! ')
            break
        else:
            print('нет такой команды...')


if __name__ == '__main__':
    user_interface()
