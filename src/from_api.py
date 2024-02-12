from abc import ABC, abstractmethod
import requests

URL_HH_RU = 'https://api.hh.ru/vacancies?&area=1&only_with_salary=true'


class VacanciesFromApi(ABC):
    @abstractmethod
    def get_vacancies(self, text, salary, per_page):
        pass


class HHRuApi(VacanciesFromApi):
    """
    Класс для работы с API сервиса HH.ru
    """

    def __init__(self):
        self.__data_api = None
        self.response_keys = {'text': '', 'salary': '', 'per_page': ''}

    def get_vacancies(self, text: str, salary: str, per_page: str):
        """
        Получение вакансий в формате .json по ключам: ключевое слово, предполагаемая зарплата, количество вакансий.
        Если пользователь не указал количество вакансий, то берутся максимально возможные 100 с одного запроса.
        Если пользователь не указал предполагаемую зарплату, то берется 100
        :param text: str
        :param salary: str
        :param per_page: str
        :return: data
        """
        self.response_keys['text'] = text
        self.response_keys['salary'] = salary
        self.response_keys['per_page'] = per_page
        response = requests.get(URL_HH_RU, self.response_keys)
        self.__data_api = response.json()
        return self.__data_api

    @property
    def data_api(self):
        return self.__data_api
