import json


class SaverUser:
    """
    Класс загрузки из файла и сохранения в файл найденной информации
    """
    data_dict = {}
    name_vacancy = []

    def __init__(self):
        self.encoding = 'utf-8'
        self.ident = 2
        self.ensure_ascii = False

    def load_vacancy(self, path_to_file: str) -> dict:
        """
        Загрузка данных из .json файла
        :param path_to_file: str
        :return: dict
        """
        with open(path_to_file, encoding=self.encoding) as file:
            data = json.load(file)
        return data

    def save_vacancy(self, data: dict, path_to_file: str) -> None:
        """
        Запись данных в .json файл
        :param data: dict
        :param path_to_file: str
        :return: file.json
        """
        with open(path_to_file, 'w', encoding=self.encoding) as file:
            json.dump(data, file, indent=self.ident, ensure_ascii=self.ensure_ascii)

    def delete_user_save(self, path_to_file: str) -> None:
        """
        Очистка файла
        :param path_to_file:
        :return: None
        """
        file = open(path_to_file, 'w')
        file.close()
