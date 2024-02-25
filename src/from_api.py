import requests

URL_HH_RU = 'https://api.hh.ru/vacancies'


class HHRuApi:
    """
    Класс для работы с API сервиса HH.ru
    """
    def __init__(self):
        self.__data_api = None
        self.__response_keys = {'areas': 113, 'area': 1, 'only_with_salary': True, 'text': '', 'salary': '',
                                'per_page': 100}

    def __str__(self) -> str:
        """
        Строка с названием сервиса
        :return: str
        """
        return 'HH.ru'

    def get_vacancies_by_keys(self, text: str, salary: str) -> dict:
        """
        Получение вакансий в формате .json по ключам: ключевое слово, предполагаемая зарплата, количество вакансий.
        :param text: str
        :param salary: str
        :return: dict
        """
        self.__response_keys['text'] = text
        self.__response_keys['salary'] = salary
        self.__data_api = HHRuApi.__get_response(self)
        return self.__data_api

    @staticmethod
    def get_status_code() -> bool:
        """
        Проверка доступности сервиса
        :return: bool
        """
        response = requests.get(URL_HH_RU)
        if response.status_code >= 400:
            return False
        return True

    def __get_response(self) -> dict:
        """
        Получение данных с сайта
        :return: dict
        """
        response = requests.get(URL_HH_RU, self.__response_keys)
        return response.json()
