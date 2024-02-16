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
    def load_vacancy(self, path_to_file) -> json:
        """
        Загрузка данных из .json файла
        :param path_to_file: str
        :return: json
        """
        with open(path_to_file, encoding='utf-8') as file:
            data = json.load(file)
        return data

    def save_vacancy(self, data, path_to_file):
        """
        Запись данных в .json файл
        :param data: json
        :param path_to_file: data, str
        :return: file.json
        """
        with open(path_to_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def delete_user_save(self, path_to_file):
        file = open(path_to_file, 'w')
        file.close()
