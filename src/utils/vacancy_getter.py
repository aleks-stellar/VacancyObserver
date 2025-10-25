from pathlib import Path
from typing import List, Dict


def write_vacancies_by_keyword(keyword: str, path: Path) -> List[Dict]:
    """
    Функция, получающая все вакансии от API по ключевому слову методом последовательных запросов
    :param keyword: Ключевое слово для поиска
    :param path: Путь к файлу для сохранения вакансий
    :return: Список вакансий
    """
    # Тут идем циклом с запросами (метод get_vacancies) и с per_page = 100 получаем все вакансии от АПИ.
    # Потом с помощью метода add_vacancy_data класса JSONWorker сохраняем вакансии в файл по пути path.
