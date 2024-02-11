from abc import ABC, abstractmethod
import requests


class VacanciesFromApi(ABC):
    @abstractmethod
    def get_vacancies(self, text, salary, per_page):
        pass


URL_HH_RU = 'https://api.hh.ru/vacancies?&area=1&only_with_salary=true'


class HHRuApi(VacanciesFromApi):
    def __init__(self):
        self.__data_api = None
        self.response_keys = {'text': '', 'salary': 0, 'per_page': ''}

    def get_vacancies(self, text, salary, per_page):
        if not per_page.isdigit() or int(per_page) > 100:
            per_page = 100
        self.response_keys['text'] = text
        self.response_keys['salary'] = salary
        self.response_keys['per_page'] = per_page
        response = requests.get(URL_HH_RU, self.response_keys)
        self.__data_api = response.json()
        return self.__data_api

    @property
    def data_api(self):
        return self.__data_api
