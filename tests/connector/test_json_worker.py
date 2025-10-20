import json
import pathlib
from typing import Dict

from src.connector.json_worker import JSONWorker


def test_init_and_validation() -> None:
    """Тестируем инициализацию объектов класса JSONWorker а также валидацию пути и имени внутри инициализации"""
    worker = JSONWorker()
    assert worker.full_path == pathlib.Path(__file__).parent.parent.parent / "data" / "vacancies.json"

    worker = JSONWorker(file_name="vacancies_data")
    assert worker.full_path == pathlib.Path(__file__).parent.parent.parent / "data" / "vacancies_data.json"

    worker = JSONWorker(path="Python/VacancyObserver")
    assert worker.full_path == pathlib.Path("Python/VacancyObserver/vacancies.json")

    worker = JSONWorker(path="Python/VacancyObserver", file_name="data.json")
    assert worker.full_path == pathlib.Path("Python/VacancyObserver/data.json")

    worker = JSONWorker(path="Python/Vacancy", file_name="data.json")
    assert worker.full_path == pathlib.Path("Python/Vacancy/data.json")


def test_add_vacancy_data(tmp_path, vacancy_data1: Dict[str, str | Dict]) -> None:
    """Проверяем работу метода add_vacancy_data"""
    tmp_file_name = "test.json"
    worker = JSONWorker(path=tmp_path, file_name=tmp_file_name)

    # Добавляем данные
    worker.add_vacancy_data(vacancy_data1)

    # Читаем данные из полного пути к файлу
    data = worker.get_vacancy_data()

    assert isinstance(data, list)
    assert data == [vacancy_data1]
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
    assert data == [vacancy_data1, vacancy_data2]
    assert data[0]["name"] == "Python Developer"
    assert data[1]["name"] == "Web Developer"


def test_check_for_duplicates(
        tmp_path,
        vacancy_data1: Dict[str, str | Dict]
) -> None:
    """Проверяем, что JSON-файл не сохраняем дубли вакансий"""
    worker = JSONWorker(path=tmp_path)

    worker.add_vacancy_data(vacancy_data1)
    worker.add_vacancy_data(vacancy_data1)

    data = worker.get_vacancy_data()

    assert isinstance(data, list)
    assert data == [vacancy_data1]
    assert data[0]["name"] == "Python Developer"


def test_get_vacancy_data(tmp_path, vacancy_data1, vacancy_data2) -> None:
    """Проверяем работу метода get_vacancy_data"""
    worker = JSONWorker(path=tmp_path)
    worker.add_vacancy_data(vacancy_data1)
    worker.add_vacancy_data(vacancy_data2)

    vacancy_data = worker.get_vacancy_data()
    assert isinstance(vacancy_data, list)
    assert vacancy_data == [vacancy_data1, vacancy_data2]
    assert vacancy_data[0]["name"] == "Python Developer"


def test_get_vacancy_data_file_not_exist(tmp_path) -> None:
    """Проверяем работу метода get_vacancy_data при обращении к несуществующему файлу"""
    worker = JSONWorker(path=tmp_path)

    if worker.full_path.exists():
        worker.full_path.unlink()

    vacancy_data = worker.get_vacancy_data()
    assert vacancy_data == []


def test_get_vacancy_data_empty_file(tmp_path) -> None:
    """Проверяем корректность при пустом файле"""
    worker = JSONWorker(path=tmp_path)
    worker.full_path.touch()

    result = worker.get_vacancy_data()
    assert result == []


def test_delete_vacancy(tmp_path, vacancy_data1, vacancy_data2) -> None:
    """Проверяем работу метода delete_vacancy_data"""
    worker = JSONWorker(path=tmp_path)
    worker.add_vacancy_data(vacancy_data1)
    worker.add_vacancy_data(vacancy_data2)
    worker.delete_vacancy_data(123456)
    data = worker.get_vacancy_data()

    assert data == [vacancy_data2]


def test_delete_method_from_empty_file(tmp_path) -> None:
    """Проверяем корректность работы метода при попытке удалить вакансию из пустого файла"""
    worker = JSONWorker(path=tmp_path)
    worker.full_path.touch()
    worker.delete_vacancy_data(123456)

    assert worker.get_vacancy_data() == []
