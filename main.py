import os

from src.from_api import HHRuApi
from src.menu import MenuUser
from src.vacancies import Vacancy, VacancyFromFile
from src.saver import SaverUser

path_data_file = 'data/data_api.json'


def user_main():
    """
    Функция для взаимодействия с пользователем
    :return: None
    """
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
            menu = MenuUser()
            Vacancy.list_vacancies = []
            menu.get_separator()
            if hh_ru.get_status_code() is False:
                menu.get_answer(1)
                break
            menu.get_key_city_from_find()
            menu.get_key_world_for_find()
            menu.get_key_salary_for_find()
            data = hh_ru.get_vacancies_by_keys(menu.key_city, menu.key_world, menu.key_salary)
            Vacancy.get_vacancy(data)
            if len(Vacancy.list_vacancies) == 0:
                menu.get_answer(0)
            else:
                num = menu.get_top_from_find(Vacancy.list_vacancies)
                Vacancy.list_vacancies = Vacancy.get_top_vacancies(Vacancy.list_vacancies, num)
                Vacancy.get_print_list_vacancies(Vacancy.list_vacancies)
                if menu.get_answer_for_save() is True:
                    if os.path.getsize(path_data_file) != 0:
                        SaverUser.data_dict = saver.load_data(path_data_file)
                    for i in Vacancy.list_vacancies:
                        save_list.append(i.__dict__)
                    SaverUser.data_dict[menu.key_world] = save_list
                    save_list = []
                    Vacancy.list_vacancies = []
                    saver.save_vacancy(SaverUser.data_dict, path_data_file)
        elif command == '2':
            menu.get_separator()
            Vacancy.list_vacancies = []
            for key, values in saver.load_data(path_data_file).items():
                saver.name_vacancy.append(key)
                VacancyFromFile.get_vacancy(values)
            VacancyFromFile.get_print_list_vacancies(Vacancy.list_vacancies)
            menu.get_name_vacancy_from_file(saver.name_vacancy)
            saver.name_vacancy = []
        elif command == '3':
            saver.delete_user_save(path_data_file)
        elif command == '0':
            menu.get_answer(2)
            break
        else:
            menu.get_answer(3)


if __name__ == '__main__':
    user_main()
