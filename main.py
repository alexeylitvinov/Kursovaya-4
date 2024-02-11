from src.from_api import HHRuApi
from src.vacancies import Vacancies

key_worlds = ''
salary = ''
number_vacancies = ''


def user_interface():
    global key_worlds
    global salary
    global number_vacancies
    print('Привет! Займемся поиском вакансий на HH.ru ')
    print('===========================================================================================================')
    while True:
        print('1 - Нажмите для поиска вакансий ')
        print('0 - Нажмите для для выхода из программы ')
        command = input('Введите команду: ')
        if command == '1':
            key_worlds = input('Введите ключевые слова для поиска вакансий: ')
            salary = input('Введите предполагаемую зарплату : ')
            number_vacancies = input('Введите сколько вакансий показать: ')
            hh_ru = HHRuApi()
            data = hh_ru.get_vacancies(key_worlds, salary, number_vacancies)
            vac = None
            for i in data['items']:
                vac = Vacancies(i)
            print('==================================================================================================')
            for i in vac.list_vacancies:
                i.get_print_class_field()
                print('==============================================================================================')
            print('==============================================================================================')
        elif command == '0':
            print('Всего хорошего! ')
            break
        else:
            print('нет такой команды...')


if __name__ == '__main__':
    user_interface()
