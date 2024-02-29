from src.saver import SaverUser


class MenuUser:
    """
    Класс пользовательского меню
    """
    load_city_data = SaverUser()
    data_city = load_city_data.load_data('data/city.json')

    def __init__(self):
        self.__num_answer = None
        self.__command = None
        self.key_city = None
        self.key_world = None
        self.key_salary = None
        self.top_vacancies = None

    @staticmethod
    def get_hello(string: str):
        """
        Вывод на экран приветствия
        :param string: str
        :return: None
        """
        print(f'Привет! Займемся поиском вакансий на {string}')

    @staticmethod
    def get_main_menu() -> None:
        """
        Вывод на экран основного меню
        :return: None
        """
        print('1 - Нажмите для поиска вакансий ')
        print('0 - Нажмите для для выхода из программы ')

    @staticmethod
    def get_main_menu_second() -> None:
        """
        Вывод на экран второстепенного меню
        :return: None
        """
        print('Есть сохраненные результаты предыдущего поиска')
        print('2 - Нажмите для загрузки сохраненных данных из файла')
        print('3 - Очистить предыдущие результаты поиска')

    @staticmethod
    def get_answer_for_save() -> bool:
        """
        Вывод на экран предложения о сохранении результатов поиска
        :return: bool
        """
        answer = input(
            'Сохранить найденные данные в файл? Нажмите "s" чтобы сохранить, чтобы продолжить нажмите любую клавишу:  ')
        if answer == 'ы' or answer == 's':
            return True
        return False

    @staticmethod
    def get_separator() -> None:
        """
        Вывод на экран декоративного разделителя
        :return: None
        """
        print('=' * 160)

    @staticmethod
    def get_name_vacancy_from_file(data: list):
        print('Ключевые слова предыдущих сохраненных поисков:', *data)
        MenuUser.get_separator()

    def get_command(self) -> str:
        """
        Вывод на экран ввода команды пользователя
        :return: str
        """
        self.__command = input('Введите команду: ')
        return self.__command

    def get_answer(self, num_answer: int) -> None:
        """
        Список ответов пользователю. Возвращаем ответ (элемент списка)
        :param num_answer: int
        :return: None
        """
        answer_list = [
            'По таким критериям ничего не найдено',
            'Сервис недоступен продолжение работы программы невозможно',
            'Всего хорошего!',
            'нет такой команды...'
        ]
        self.__num_answer = answer_list[num_answer]
        print(f'{self.__num_answer}')

    def get_key_city_from_find(self) -> str:
        while True:
            user_input = input('Введите город для поиска вакансий (кириллицей): ').title()
            for i in MenuUser.data_city:
                for key, value in i.items():
                    if value == user_input:
                        self.key_city = key
            if self.key_city is None:
                print('Не верно введено название города или такой город не найден...')
            else:
                break
        return self.key_city

    def get_key_world_for_find(self) -> str:
        """
        Получение ключевого слова от пользователя по вакансиям с проверкой правильности введенных данных
        :return: str
        """
        while True:
            user_input = input('Введите ключевые слова для поиска вакансий: ')
            if user_input.isdigit() or user_input is None:
                print('Не верно введено ключевое слово...')
            else:
                self.key_world = user_input
                break
        return self.key_world

    def get_key_salary_for_find(self) -> int:
        """
        Получение ключевого слова от пользователя по зарплате с проверкой правильности введенных данных
        :return: int
        """
        while True:
            user_input = input('Введите предполагаемую зарплату : ')
            if user_input.isnumeric() is False or user_input is None or int(user_input) <= 0:
                print('На ввод доступны только числа...')
            else:
                self.key_salary = int(user_input)
                break
        return self.key_salary

    def get_top_from_find(self, data_list: list) -> int:
        """
        Получение количества топ вакансий от пользователя с проверкой правильности введенных данных
        :return: int
        """
        while True:
            user_input = input('Введите сколько вакансий показать (на экран выводятся топ N вакансий по зарплате): ')
            if user_input.isnumeric() is False or user_input is None or int(user_input) > 100 or int(user_input) <= 0:
                print('На ввод доступны только числа. Максимальное значение 100...')
            elif int(user_input) > len(data_list):
                print(f'Найдено {len(data_list)} вакансий. Вы пытаетесь посмотреть больше...')
            else:
                self.top_vacancies = int(user_input)
                break
        MenuUser.get_separator()
        return self.top_vacancies
