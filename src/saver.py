from abc import ABC, abstractmethod
import json


class Saver(ABC):
    pass

    @abstractmethod
    def load_vacancy(self, path_to_file):
        pass

    @abstractmethod
    def save_vacancy(self, data, path_to_file):
        pass

    @abstractmethod
    def delete_user_save(self, path_to_file):
        pass


class SaverUser(Saver):
    """
    Класс загрузки из файла и сохранения в файл найденной информации
    """
    def load_vacancy(self, path_to_file: str) -> dict:
        """
        Загрузка данных из .json файла
        :param path_to_file: str
        :return: dict
        """
        with open(path_to_file, encoding='utf-8') as file:
            data = json.load(file)
        return data

    def save_vacancy(self, data: dict, path_to_file: str) -> None:
        """
        Запись данных в .json файл
        :param data: dict
        :param path_to_file: str
        :return: file.json
        """
        with open(path_to_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def delete_user_save(self, path_to_file: str) -> None:
        """
        Очистка файла
        :param path_to_file:
        :return: None
        """
        file = open(path_to_file, 'w')
        file.close()
