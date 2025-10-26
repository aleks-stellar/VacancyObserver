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
    :return: Список вакансий
    """
    hh_api = HeadHunterAPI()
    worker = JSONWorker(path=str(path), file_name=keyword)
    while True:
        start = 0
        vacancy_portion = hh_api.get_vacancies(keyword=keyword, vacancies_amount=100, start_page=start)
        for vacancy_api in vacancy_portion:
            vacancy_obj = BaseVacancy(
                title=vacancy_api["name"],
                link=vacancy_api["alternate_url"],
                salary=vacancy_api["salary"],
                brief_desc=vacancy_api["snippet"]["requirement"]
            )
            vacancy_dict = vacancy_obj.get_vacancy()
            worker.add_vacancy_data(vacancy_dict)
