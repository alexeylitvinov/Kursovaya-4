import os

from src.from_api import HHRuApi
from src.menu import MenuUser
from src.vacancies import Vacancies, VacanciesFromFile
from src.saver import SaverUser

path_data_file = 'data/data_api.json'


def user_main():
    """
    Функция для взаимодействия с пользователем
    :return: None
    """
    vacancies = None
    hh_ru = HHRuApi()
    save_list = []
    menu = MenuUser()
    saver = SaverUser()
    menu.get_hello(hh_ru.__str__())
    menu.get_separator()

    while True:
        menu.get_main_menu()
        if os.path.getsize(path_data_file) != 0:
            menu.get_main_menu_second()
        command = menu.get_command()
        if command == '1':
            Vacancies.list_vacancies = []
            menu.get_separator()
            if hh_ru.get_status_code() == 'no service':
                menu.get_answer(1)
                break
            menu.get_key_world_for_find()
            menu.get_key_salary_for_find()
            menu.get_per_page_for_find()
            data = hh_ru.get_vacancies(*menu.get_all_keys())
            try:
                for i in data['items']:
                    vacancies = Vacancies()
                    vacancies.get_vacancies(i)
            except KeyError:
                menu.get_answer(0)
            else:
                if not vacancies:
                    menu.get_answer(0)
                else:
                    Vacancies.list_vacancies = (
                        sorted(vacancies.list_vacancies, key=lambda x: x.salary_from, reverse=True))
                    vacancies.get_print_list_vacancies()
                    if menu.get_answer_for_save() is True:
                        for i in vacancies.list_vacancies:
                            save_list.append(i.__dict__)
                        saver.save_vacancy(save_list, path_data_file)
        elif command == '2':
            menu.get_separator()
            Vacancies.list_vacancies = []
            for i in saver.load_vacancy(path_data_file):
                vacancies = VacanciesFromFile()
                vacancies.get_vacancies(i)
            vacancies.get_print_list_vacancies()
        elif command == '3':
            saver.delete_user_save(path_data_file)
        elif command == '0':
            menu.get_answer(2)
            break
        else:
            menu.get_answer(3)


if __name__ == '__main__':
    user_main()
