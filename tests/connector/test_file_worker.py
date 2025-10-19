from abc import ABC

import pytest

from src.connector.file_worker import FileWorker


def test_file_worker_is_abstract() -> None:
    """Проверяем, что класс FileWorker является абстрактным"""
    assert issubclass(FileWorker, ABC)


def test_file_worker_has_abstract_methods() -> None:
    """Проверяем, что у FileWorker есть абстрактные методы"""
    abstract_methods = FileWorker.__abstractmethods__
    assert "get_vacancy_data" in abstract_methods
    assert "add_vacancy_data" in abstract_methods
    assert "delete_vacancy_data" in abstract_methods
    assert "full_path" in abstract_methods
    assert "_validate_path" in abstract_methods
    assert "_validate_name" in abstract_methods


def test_file_worker_cannot_be_instantiated() -> None:
    """Проверяем, что нельзя создать экземпляр FileWorker"""
    with pytest.raises(TypeError):
        FileWorker()  # type: ignore[abstract]
