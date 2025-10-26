from pathlib import Path
from typing import List, Dict

from src.api.hh_api import HeadHunterAPI
from src.connector.json_worker import JSONWorker
from src.vacancy.base_vacancy import BaseVacancy


def write_vacancies_by_keyword(keyword: str, path: Path) -> None:
    """
    Функция, получающая все вакансии от API по ключевому слову методом последовательных запросов
    :param keyword: Ключевое слово для поиска
    :param path: Путь к файлу для сохранения вакансий
    """
    hh_api = HeadHunterAPI()
    worker = JSONWorker(path=str(path), file_name=keyword)
    start = 0
    page_size = 100

    while True:
        try:
            vacancy_portion = hh_api.get_vacancies(
                keyword=keyword,
                vacancies_amount=page_size,
                start_page=start
            )
        except ConnectionError:
            break

        if not vacancy_portion:
            break

        for vacancy_api in vacancy_portion:
            vacancy_obj = BaseVacancy(
                title=vacancy_api["name"],
                link=vacancy_api["alternate_url"],
                salary=vacancy_api["salary"],
                brief_desc=vacancy_api["snippet"]["requirement"]
            )
            worker.add_vacancy_data(vacancy_obj.get_vacancy())

        start += len(vacancy_portion)


def write_top_vacancies_by_salary(min_salary: int, top_number: int, path: Path) -> None:
    """
    Получаем топ-N вакансий по минимальной зарплате
    """
    hh_api = HeadHunterAPI()
    worker = JSONWorker(path=str(path), file_name=f"top_{top_number}_salary_{min_salary}")

    start = 0
    page_size = 100
    all_vacancies = []

    while True:
        try:
            vacancy_portion = hh_api.get_vacancies(
                salary_from=min_salary,
                vacancies_amount=page_size,
                start_page=start
            )
        except ConnectionError as e:
            print(f"Ошибка запроса к API: {e}. Прерываем сбор вакансий.")
            break

        if not vacancy_portion:
            break

        all_vacancies.extend(vacancy_portion)
        start += len(vacancy_portion)  # учитываем реальное количество полученных вакансий

    # Фильтруем вакансии с ненулевой зарплатой и сортируем по salary["from"]
    valid_vacancies = [
        vac for vac in all_vacancies
        if vac.get("salary") and isinstance(vac["salary"], dict) and vac["salary"].get("from")
    ]

    top_vacancies = sorted(valid_vacancies, key=lambda v: v["salary"]["from"], reverse=True)[:top_number]

    # Сохраняем через JSONWorker
    for vac in top_vacancies:
        vacancy_obj = BaseVacancy(
            title=vac["name"],
            link=vac["alternate_url"],
            salary=vac["salary"],
            brief_desc=vac["snippet"]["requirement"]
        )
        worker.add_vacancy_data(vacancy_obj.get_vacancy())
