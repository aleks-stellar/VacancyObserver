from unittest.mock import patch
from pathlib import Path
import pytest

from src.utils.vacancy_getter import write_vacancies_by_keyword, write_top_vacancies_by_salary

def test_write_vacancies_by_keyword(tmp_path, vacancies_list):
    """Проверяем, что функция корректно обрабатывает вакансии и вызывает add_vacancy_data"""

    kwd = "Python"
    fake_path = tmp_path / "test.json"

    # Мок данных с API: две вакансии на первой странице, пустая вторая → конец цикла
    api_response_page1 = vacancies_list["items"]
    api_response_page2 = []  # имитация конца страниц

    # Список для проверки, какие вакансии "сохраняются"
    saved_vacancies = []

    def fake_add_vacancy_data(vacancy):
        saved_vacancies.append(vacancy)

    # Мок классов
    with patch("src.utils.vacancy_getter.HeadHunterAPI") as mock_api_class, \
         patch("src.utils.vacancy_getter.JSONWorker") as mock_worker_class:

        # Мок экземпляра API
        mock_api_instance = mock_api_class.return_value

        # side_effect функция учитывает start и завершение цикла
        def fake_get_vacancies(keyword, vacancies_amount, start_page):
            if start_page == 0:
                return api_response_page1
            return []  # конец данных

        mock_api_instance.get_vacancies.side_effect = fake_get_vacancies

        # Мок экземпляра JSONWorker
        mock_worker_instance = mock_worker_class.return_value
        mock_worker_instance.add_vacancy_data.side_effect = fake_add_vacancy_data

        # Вызов тестируемой функции
        write_vacancies_by_keyword(keyword=kwd, path=fake_path)

    # Проверки
    assert len(saved_vacancies) == len(api_response_page1)
    for i, vac in enumerate(saved_vacancies):
        assert vac["name"] == api_response_page1[i]["name"]
        assert vac["alternate_url"] == api_response_page1[i]["alternate_url"]
        assert vac["salary"] == api_response_page1[i]["salary"]
        assert vac["requirement"] == api_response_page1[i]["snippet"]["requirement"]


def test_write_top_vacancies_by_salary(tmp_path):
    """Проверяем работу функции write_top_vacancies_by_salary"""
    fake_path = tmp_path / "top_vacancies.json"
    top_n = 2
    min_salary = 100000

    # Мок вакансий
    vacancies_list = [
        {"name": "Dev1", "alternate_url": "url1", "salary": {"from": 120000}, "snippet": {"requirement": "Req1"}},
        {"name": "Dev2", "alternate_url": "url2", "salary": {"from": 150000}, "snippet": {"requirement": "Req2"}},
        {"name": "Dev3", "alternate_url": "url3", "salary": {"from": 100000}, "snippet": {"requirement": "Req3"}},
    ]

    saved_vacancies = []

    def fake_add_vacancy_data(vac):
        saved_vacancies.append(vac)

    with patch("src.utils.vacancy_getter.HeadHunterAPI") as mock_api_class, \
         patch("src.utils.vacancy_getter.JSONWorker") as mock_worker_class:

        mock_api_instance = mock_api_class.return_value
        # Возвращаем все вакансии сразу, потом пустой список для завершения цикла
        mock_api_instance.get_vacancies.side_effect = [vacancies_list, []]

        mock_worker_instance = mock_worker_class.return_value
        mock_worker_instance.add_vacancy_data.side_effect = fake_add_vacancy_data

        # Вызов функции
        write_top_vacancies_by_salary(min_salary=min_salary, top_number=top_n, path=fake_path)

    # Проверяем, что добавлено top N вакансий по salary["from"]
    assert len(saved_vacancies) == top_n
    salaries = [vac["salary"]["from"] for vac in saved_vacancies]
    assert salaries == sorted(salaries, reverse=True)
