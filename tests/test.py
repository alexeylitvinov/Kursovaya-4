from src.from_api import HHRuApi
from src.vacancies import Vacancy
from src.function import delete_highlight, get_validation_text, get_validation_salary


def test_create_vacancies():
    vacancies = Vacancy()
    assert vacancies.city is None
    assert vacancies.name is None
    assert vacancies.salary_from is None
    assert vacancies.salary_to is None
    assert vacancies.currency is None
    assert vacancies.url is None
    assert vacancies.requirement is None
    assert vacancies.responsibility is None
    assert len(vacancies.list_vacancies) == 0


def test_get_vacancies():
    hh_ru = HHRuApi()
    data = hh_ru.get_vacancies_by_keys('python', '100000')
    for i in data['items']:
        vacancies = Vacancy()
        vacancies.get_vacancy(i)
    assert len(vacancies.list_vacancies) == 100


def test_delete_highlight():
    assert delete_highlight('hello<highlighttext> world</highlighttext>!') == 'hello world!'


def test_validation_text():
    text = None
    assert get_validation_text(text) == 'Не указано'


def test_validation_salary():
    text = None
    assert get_validation_salary(text) == 0
