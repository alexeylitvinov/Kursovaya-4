# __Курсовая работа ООП__

### получение вакансий с сайта HH.ru по заданным параметрам

___

### Как работать:

Запуск программы с `main.py`

#### Основное меню

`Привет! Займемся поиском вакансий на HH.ru`

`1 - Нажмите для поиска вакансий`

`0 - Нажмите для для выхода из программы`

`Введите команду: `

После ввода команды выводит предложение ввести ключевые слова для поиска.

Далее выводит список найденных вакансий по заданным параметрам с предложением сохранить

результаты поиска в файл `data_api.json`

Вакансии отсортированы по зарплате от большего к меньшему

#### Вспомогательное меню (если есть сохраненный файл предыдущих поисков)

`Есть сохраненные результаты предыдущего поиска`

`2 - Нажмите для загрузки сохраненных данных из файла`

`3 - Очистить предыдущие результаты поиска`

`Введите команду:`

После ввода команды загружает данные из файла и выводит на экран вакансии и ключевые слова предыдущих поисков которые 
были сохранены, либо очищает файл от данных

Есть проверки на корректность ввода данных