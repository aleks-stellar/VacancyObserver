from unittest.mock import Mock, patch
from src.api.hh_api import HeadHunterAPI


@patch("src.api.hh_api.requests.get")
def test_hh_api_object_init(mock_get, vacancies_list):
    """Тестируем работу метода get_vacancies"""

    mock_get.return_value.json.return_value = vacancies_list

    hh_api = HeadHunterAPI()
    vacancies = hh_api.get_vacancies("Python")

    mock_get.assert_called_once()

    assert vacancies["items"][0]["id"] == 93353083
    assert len(vacancies["items"]) == 2
