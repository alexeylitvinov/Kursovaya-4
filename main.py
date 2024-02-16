import os

from src.from_api import HHRuApi
from src.function import get_main_menu, get_main_menu_second, get_key_worlds_for_find, save_to_file, load_to_file, \
    delete_from_file
from src.vacancies import Vacancies

# from src.saver import SaverUser

path_data_file = 'data/data_api.json'


def user_main():
    """
    Функция для взаимодействия с пользователем
    :return: None
    """
    # saver = SaverUser()
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
            if hh_ru.get_status_code() == 'no service':
                print('Сервис недоступен продолжение работы программы невозможно')
                break
            data = hh_ru.get_vacancies(*get_key_worlds_for_find())
            try:
                for i in data['items']:
                    vacancies = Vacancies(i)
            except KeyError:
                print('По таким критериям ничего не найдено')
            else:
                if not vacancies:
                    print('По таким критериям ничего не найдено')
                else:
                    Vacancies.list_vacancies = sorted(vacancies.list_vacancies, key=lambda x: x.salary_from, reverse=True)
                    vacancies.get_print_list_vacancies()
                    answer = input(
                        'Сохранить найденные данные в файл? Нажмите "s" чтобы сохранить, чтобы продолжить нажмите '
                        '"ENTER"  ')
                    if answer == 'ы' or answer == 's':
                        for i in vacancies.list_vacancies:
                            save_list.append(i.__dict__)
                            print(i.__dict__)
                        save_to_file(save_list, 'data/data_api.json')
        elif command == '2':
            Vacancies.list_vacancies = []
            for i in load_to_file(path_data_file):
                vacancies = Vacancies(i)
            vacancies.get_print_list_vacancies()
        elif command == '3':
            delete_from_file(path_data_file)
        elif command == '0':
            print('Всего хорошего! ')
            break
        else:
            print('нет такой команды...')


if __name__ == '__main__':
    user_main()
