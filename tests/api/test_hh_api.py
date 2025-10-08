from unittest.mock import Mock, patch

import pytest

from src.api.hh_api import HeadHunterAPI
from src.api.base_api import BaseAPI


def test_headhunterapi_issubclass():
    """Проверяем, что класс HeadHunterAPI является подклассом класса BaseAPI"""
    assert issubclass(HeadHunterAPI,BaseAPI)


def test_abstract_methods_have_been_implemented():
    """Проверяем, что абстрактные методы были реализованы"""
    methods = HeadHunterAPI.__abstractmethods__
    assert methods == frozenset()


def test_hh_api_attributes_is_private():
    """Проверяем, что все атрибуты экземпляра класса HeadHunterAPI приватные"""
    hh_api_obj = HeadHunterAPI()
    attrs = [attr for attr in vars(hh_api_obj).keys() if not attr.startswith(f"_{hh_api_obj.__class__.__name__}__")]
    assert not attrs


@patch("src.api.hh_api.requests.get")
def test_hh_api_object_init(mock_get, vacancies_list):
    """Тестируем работу метода get_vacancies"""

    mock_get.return_value.json.return_value = vacancies_list
    mock_get.return_value.status_code = 200

    hh_api = HeadHunterAPI()
    vacancies = hh_api.get_vacancies("Python", 5)

    mock_get.assert_called_once()

    assert vacancies[0]["id"] == "93353083"
    assert len(vacancies) == 2


@patch("src.api.hh_api.requests.get")
def test_hh_api_status_code_check(mock_get, vacancies_list):
    """Проверяем, что при плохом статус-коде выбрасывается исключение"""
    mock_response = mock_get.return_value
    mock_response.status_code = 404

    with pytest.raises(ConnectionError):
        HeadHunterAPI().get_vacancies("Python", 5)


@patch("src.api.hh_api.requests.get")
def test_hh_api_request_params(mock_get):
    """Проверяем, что метод get_vacancies формирует параметры text и per_page"""

    # Настраиваем поведение мока
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"items": []}

    hh_api = HeadHunterAPI()
    hh_api.get_vacancies("Python", 5)

    # Проверяем, что метод requests.get был вызван
    mock_get.assert_called_once()

    # Извлекаем аргументы, с которыми был вызван requests.get
    _, kwargs = mock_get.call_args

    params = kwargs.get("params", {})
    assert "text" in params, "Параметр 'text' отсутствует в запросе"
    assert "per_page" in params, "Параметр 'per_page' отсутствует в запросе"
