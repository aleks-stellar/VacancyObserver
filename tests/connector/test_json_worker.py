import json
from pathlib import WindowsPath
from typing import Dict

from src.connector.json_worker import JSONWorker


def test_init_and_validation() -> None:
    """Тестируем инициализацию объектов класса JSONWorker а также валидацию пути и имени внутри инициализации"""
    worker = JSONWorker()
    assert worker.full_path == WindowsPath("D:/Science/Python/VacancyObserver/data/vacancies.json")

    worker = JSONWorker(file_name="vacancies_data")
    assert worker.full_path == WindowsPath("D:/Science/Python/VacancyObserver/data/vacancies_data.json")

    worker = JSONWorker(path="D:/Science/Python/VacancyObserver")
    assert worker.full_path == WindowsPath("D:/Science/Python/VacancyObserver/vacancies.json")

    worker = JSONWorker(path="D:/Science/Python/VacancyObserver", file_name="data.json")
    assert worker.full_path == WindowsPath("D:/Science/Python/VacancyObserver/data.json")

    worker = JSONWorker(path="D:/Python/Vacancy", file_name="data.json")
    assert worker.full_path == WindowsPath("D:/Python/Vacancy/data.json")


def test_class_attributes() -> None:
    """Проверяем атрибуты класса"""
    worker = JSONWorker()
    assert worker.DEFAULT_NAME == "vacancies.json"
    assert worker.DEFAULT_PATH == WindowsPath("D:/Science/Python/VacancyObserver/data")


def test_add_vacancy_data(tmp_path, vacancy_data1: Dict[str, str | Dict]) -> None:
    """Проверяем работу метода add_vacancy_data"""
    tmp_file_name = "test.json"
    worker = JSONWorker(path=tmp_path, file_name=tmp_file_name)

    # Добавляем данные
    worker.add_vacancy_data(vacancy_data1)

    # Читаем данные из полного пути к файлу
    with open(worker.full_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["name"] == "Python Developer"


def test_add_two_vacancies_data(
        tmp_path,
        vacancy_data1: Dict[str, str | Dict],
        vacancy_data2: Dict[str, str | Dict]
) -> None:
    """Проверяем работу метода add_vacancy_data при добавлении двух вакансий"""
    tmp_file_name = "test.json"
    worker = JSONWorker(path=tmp_path, file_name=tmp_file_name)

    worker.add_vacancy_data(vacancy_data1)
    worker.add_vacancy_data(vacancy_data2)

    with open(worker.full_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["name"] == "Python Developer"
    assert data[1]["name"] == "Web Developer"
