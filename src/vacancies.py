from src.function import delete_highlight, get_validation


class Vacancies:
    """
    Класс вакансий
    """
    list_vacancies = []

    def __init__(self, data_api):
        """
        Инициализация класса. Делаем проверку на наличие ключей в случае загрузки данных из файла
        :param data_api: dict
        """

        self.name = data_api['name']
        if data_api.get('salary') is None:
            self.salary_from = data_api['salary_from']
        else:
            self.salary_from = get_validation(data_api['salary']['from'])
        if data_api.get('salary') is None:
            self.salary_to = data_api['salary_to']
        else:
            self.salary_to = get_validation(data_api['salary']['to'])
        if data_api.get('salary') is None:
            self.currency = data_api['currency']
        else:
            self.currency = data_api['salary']['currency']
        if data_api.get('alternate_url') is None:
            self.url = data_api['url']
        else:
            self.url = data_api['alternate_url']
        if data_api.get('snippet') is None:
            self.requirement = data_api['requirement']
        else:
            self.requirement = delete_highlight(get_validation(data_api['snippet']['requirement']))
        if data_api.get('snippet') is None:
            self.responsibility = data_api['responsibility']
        else:
            self.responsibility = delete_highlight(get_validation(data_api['snippet']['responsibility']))
        self.list_vacancies.append(self)

    def get_print_class_field(self):
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
