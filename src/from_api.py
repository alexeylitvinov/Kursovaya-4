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
        self.__response_keys = {'text': '', 'salary': '', 'per_page': ''}

    def __str__(self):
        return f'HH.ru'

    def get_vacancies(self, text: str, salary: str, per_page: str) -> dict:
        """
        Получение вакансий в формате .json по ключам: ключевое слово, предполагаемая зарплата, количество вакансий.
        :param text: str
        :param salary: str
        :param per_page: str
        :return: dict
        """
        self.__response_keys['text'] = text
        self.__response_keys['salary'] = salary
        self.__response_keys['per_page'] = per_page
        self.__data_api = HHRuApi.__get_response(self)
        return self.__data_api

    @staticmethod
    def get_status_code() -> str:
        """
        Проверка доступности сервиса
        :return: str
        """
        response = requests.get(URL_HH_RU)
        if response.status_code >= 400:
            return f'no service'

    def __get_response(self) -> dict:
        """
        Получение данных с сайта
        :return: dict
        """
        response = requests.get(URL_HH_RU, self.__response_keys)
        return response.json()