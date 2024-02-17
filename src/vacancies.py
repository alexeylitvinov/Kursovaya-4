from src.function import delete_highlight, get_validation_text, get_validation_salary
from src.menu import MenuUser


class Vacancies:
    """
    Класс получения вакансий из запроса на сайт
    """
    list_vacancies = []

    def __init__(self):
        self.name = None
        self.salary_from = None
        self.salary_to = None
        self.currency = None
        self.url = None
        self.requirement = None
        self.responsibility = None

    def get_vacancies(self, data_api: dict):
        """
        Получение полей класса из запроса на сайт
        :param data_api: dict
        :return: class field
        """
        self.name = data_api['name']
        self.salary_from = get_validation_salary(data_api['salary']['from'])
        self.salary_to = get_validation_salary(data_api['salary']['to'])
        self.currency = data_api['salary']['currency']
        self.url = data_api['alternate_url']
        self.requirement = delete_highlight(get_validation_text(data_api['snippet']['requirement']))
        self.responsibility = delete_highlight(get_validation_text(data_api['snippet']['responsibility']))
        self.list_vacancies.append(self)

    def get_print_class_field(self) -> None:
        """
        Выводим на экран поля класса
        :return: None
        """
        print(self.name)
        print(self.salary_from)
        print(self.salary_to)
        print(self.currency)
        print(self.url)
        print(self.requirement)
        print(self.responsibility)

    def get_print_list_vacancies(self) -> None:
        """
        Вывод на экран списка полей класса
        :return: None
        """
        for i in self.list_vacancies:
            i.get_print_class_field()
            MenuUser.get_separator()


class VacanciesFromFile(Vacancies):
    """
    Класс получения вакансий из сохраненного файла
    """
    def __init__(self):
        super().__init__()

    def get_vacancies(self, data_api: dict):
        """
        Получение полей класса из сохраненного файла
        :param data_api: dict
        :return: class field
        """
        self.name = data_api['name']
        self.salary_from = data_api['salary_from']
        self.salary_to = data_api['salary_to']
        self.currency = data_api['currency']
        self.url = data_api['url']
        self.requirement = data_api['requirement']
        self.responsibility = data_api['responsibility']
        self.list_vacancies.append(self)
