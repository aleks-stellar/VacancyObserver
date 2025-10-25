import json
from pathlib import Path
from typing import Dict

from src.connector.json_worker import JSONWorker


def test_init_and_validation(tmp_path: Path) -> None:
    """Тестируем инициализацию объектов класса JSONWorker а также валидацию пути и имени внутри инициализации"""
    default_path = tmp_path / "data"
    worker = JSONWorker(path=str(default_path))
    assert worker.full_path == default_path / "vacancies.json"

    worker = JSONWorker(path=str(tmp_path), file_name="vacancies_data")
    assert worker.full_path == tmp_path / "vacancies_data.json"

    nested_path = tmp_path / "Python" / "VacancyObserver"
    worker = JSONWorker(path=str(nested_path))
    assert worker.full_path == nested_path / "vacancies.json"

    worker = JSONWorker(path=str(nested_path), file_name="data.json")
    assert worker.full_path == nested_path / "data.json"

    another_path = tmp_path / "Python" / "Vacancy"
    worker = JSONWorker(path=str(another_path), file_name="data.json")
    assert worker.full_path == another_path / "data.json"


def test_add_vacancy_data(tmp_path: Path, vacancy_data1: Dict[str, str | Dict]) -> None:
    """Проверяем работу метода add_vacancy_data"""
    tmp_file_name = "test.json"
    worker = JSONWorker(path=str(tmp_path), file_name=tmp_file_name)

    # Добавляем данные
    worker.add_vacancy_data(vacancy_data1)

    # Читаем данные из полного пути к файлу
    data = worker.get_vacancy_data()

    assert isinstance(data, list)
    assert data == [vacancy_data1]
    assert data[0]["name"] == "Python Developer"


def test_add_two_vacancies_data(
        tmp_path: Path,
        vacancy_data1: Dict[str, str | Dict],
        vacancy_data2: Dict[str, str | Dict]
) -> None:
    """Проверяем работу метода add_vacancy_data при добавлении двух вакансий"""
    tmp_file_name = "test.json"
    worker = JSONWorker(path=str(tmp_path), file_name=tmp_file_name)

    worker.add_vacancy_data(vacancy_data1)
    worker.add_vacancy_data(vacancy_data2)

    with open(worker.full_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert isinstance(data, list)
    assert data == [vacancy_data1, vacancy_data2]
    assert data[0]["name"] == "Python Developer"
    assert data[1]["name"] == "Web Developer"


def test_check_for_duplicates(
        tmp_path: Path,
        vacancy_data1: Dict[str, str | Dict]
) -> None:
    """Проверяем, что JSON-файл не сохраняем дубли вакансий"""
    worker = JSONWorker(path=str(tmp_path))

    worker.add_vacancy_data(vacancy_data1)
    worker.add_vacancy_data(vacancy_data1)

    data = worker.get_vacancy_data()

    assert isinstance(data, list)
    assert data == [vacancy_data1]
    assert data[0]["name"] == "Python Developer"


def test_get_vacancy_data(
        tmp_path: Path,
        vacancy_data1: Dict[str, str | Dict],
        vacancy_data2: Dict[str, str | Dict]
) -> None:
    """Проверяем работу метода get_vacancy_data"""
    worker = JSONWorker(path=str(tmp_path))
    worker.add_vacancy_data(vacancy_data1)
    worker.add_vacancy_data(vacancy_data2)

    vacancy_data = worker.get_vacancy_data()
    assert isinstance(vacancy_data, list)
    assert vacancy_data == [vacancy_data1, vacancy_data2]
    assert vacancy_data[0]["name"] == "Python Developer"


def test_get_vacancy_data_file_not_exist(tmp_path: Path) -> None:
    """Проверяем работу метода get_vacancy_data при обращении к несуществующему файлу"""
    worker = JSONWorker(path=str(tmp_path))

    if worker.full_path.exists():
        worker.full_path.unlink()

    vacancy_data = worker.get_vacancy_data()
    assert vacancy_data == []


def test_get_vacancy_data_empty_file(tmp_path: Path) -> None:
    """Проверяем корректность при пустом файле"""
    worker = JSONWorker(path=str(tmp_path))
    worker.full_path.touch()

    result = worker.get_vacancy_data()
    assert result == []


def test_get_vacancy_data_custom_path_empty_file(tmp_path: Path) -> None:
    """Проверяем корректность работы с пустым файлом при указании собственного пути"""
    worker = JSONWorker(path=str(tmp_path))
    worker.full_path.touch()

    result = worker.get_vacancy_data(path=tmp_path)
    assert result == []


def test_get_vacancy_data_custom_path(
        tmp_path: Path,
        vacancy_data1: Dict[str, str | Dict],
        vacancy_data2: Dict[str, str | Dict]
) -> None:
    """Проверяем корректность работы при указании собственного пути"""
    worker = JSONWorker(path=str(tmp_path), file_name="test.json")
    worker.full_path.touch()
    worker.add_vacancy_data(vacancy_data1)
    worker.add_vacancy_data(vacancy_data2)

    result = worker.get_vacancy_data(path=tmp_path / "test.json")
    assert result == [vacancy_data1, vacancy_data2]


def test_delete_vacancy(
        tmp_path: Path,
        vacancy_data1: Dict[str, str | Dict],
        vacancy_data2: Dict[str, str | Dict]
) -> None:
    """Проверяем работу метода delete_vacancy_data"""
    worker = JSONWorker(path=str(tmp_path))
    worker.add_vacancy_data(vacancy_data1)
    worker.add_vacancy_data(vacancy_data2)
    worker.delete_vacancy_data(123456)
    data = worker.get_vacancy_data()

    assert data == [vacancy_data2]


def test_delete_method_from_empty_file(tmp_path: Path) -> None:
    """Проверяем корректность работы метода при попытке удалить вакансию из пустого файла"""
    worker = JSONWorker(path=str(tmp_path))
    worker.full_path.touch()
    worker.delete_vacancy_data(123456)

    assert worker.get_vacancy_data() == []
