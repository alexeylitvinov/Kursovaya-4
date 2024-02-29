from src.function import delete_highlight, get_validation_text, get_validation_salary
from src.menu import MenuUser


class Vacancy:
    """
    Класс получения вакансий из запроса на сайт
    """
    list_vacancies = []

    def __init__(self, city, name, salary_from, salary_to, currency, url, requirement, responsibility):
        self.city = city
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.url = url
        self.requirement = requirement
        self.responsibility = responsibility
        Vacancy.list_vacancies.append(self)

    @classmethod
    def get_vacancy(cls, data_api: dict):
        """
        Получение полей класса из запроса на сайт
        :param data_api: dict
        :return: class field
        """
        for i in data_api['items']:
            city = i['area']['name']
            name = i['name']
            salary_from = get_validation_salary(i['salary']['from'])
            salary_to = get_validation_salary(i['salary']['to'])
            currency = i['salary']['currency']
            url = i['alternate_url']
            requirement = delete_highlight(get_validation_text(i['snippet']['requirement']))
            responsibility = delete_highlight(get_validation_text(i['snippet']['responsibility']))
            cls(city, name, salary_from, salary_to, currency, url, requirement, responsibility)

    def get_print_class_field(self) -> None:
        """
        Выводим на экран поля класса
        :return: None
        """
        print(self.city)
        print(self.name)
        print(self.salary_from)
        print(self.salary_to)
        print(self.currency)
        print(self.url)
        print(self.requirement)
        print(self.responsibility)

    @staticmethod
    def get_print_list_vacancies(list_vacancies: list):
        """
        Вывод на экран списка полей класса
        :return: None
        """
        for i in list_vacancies:
            i.get_print_class_field()
            MenuUser.get_separator()

    @staticmethod
    def get_top_vacancies(list_vacancies, quantity: int) -> list:
        """
        Получение топ вакансий из отсортированного списка
        :param list_vacancies: list
        :param quantity: int
        :return: list
        """
        list_vacancies.sort(key=lambda x: x.salary_from, reverse=True)
        return list_vacancies[:quantity]


class VacancyFromFile(Vacancy):
    """
    Класс получения вакансий из сохраненного файла
    """

    @classmethod
    def get_vacancy(cls, data_api: dict):
        """
        Получение полей класса из сохраненного файла
        :param data_api: dict
        :return: class field
        """
        for i in data_api:
            city = i['city']
            name = i['name']
            salary_from = i['salary_from']
            salary_to = i['salary_to']
            currency = i['currency']
            url = i['url']
            requirement = i['requirement']
            responsibility = i['responsibility']
            cls(city, name, salary_from, salary_to, currency, url, requirement, responsibility)
