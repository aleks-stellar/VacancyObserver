from unittest.mock import patch
from src.api.hh_api import HeadHunterAPI
from src.api.base_api import BaseAPI


def test_headhunterapi_issubclass():
    """Проверяем, что класс HeadHunterAPI является подклассом класса BaseAPI"""
    assert issubclass(HeadHunterAPI,BaseAPI)


def test_abstract_methods_have_been_implemented():
    """Проверяем, что абстрактные методы были реализованы"""
    methods = HeadHunterAPI.__abstractmethods__
    assert methods == frozenset()


@patch("src.api.hh_api.requests.get")
def test_hh_api_object_init(mock_get, vacancies_list):
    """Тестируем работу метода get_vacancies"""

    mock_get.return_value.json.return_value = vacancies_list

    hh_api = HeadHunterAPI()
    vacancies = hh_api.get_vacancies()

    mock_get.assert_called_once()

    assert vacancies["items"][0]["id"] == "93353083"
    assert len(vacancies["items"]) == 2
