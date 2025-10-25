import pathlib
from abc import ABC, abstractmethod
from typing import Dict, List


class FileWorker(ABC):
    """Абстрактный класс для работы чтения, записи и удаления информации о вакансиях из файла"""

    @abstractmethod
    def get_vacancy_data(self) -> List:
        """Метод для получения данных о вакансиях из файла"""
        pass

    @abstractmethod
    def add_vacancy_data(self, vacancy: Dict) -> None:
        """
        Метод для добавления данных о вакансиях в файл
        :param vacancy: Словарь с данными о вакансии
        """
        pass

    @property
    @abstractmethod
    def full_path(self) -> pathlib.Path:
        """Метод для чтения полного пути к файлу"""
        pass

    @abstractmethod
    def get_default_path(self) -> pathlib.Path:
        """Метод для чтения пути к папке по умолчания"""
        pass

    @abstractmethod
    def delete_vacancy_data(self, vacancy_id: int) -> None:
        """
        Метод для удаления данных о вакансиях из файла
        :param vacancy_id: ID вакансии
        """
        pass

    @abstractmethod
    def _validate_path(self, path_to_f: str) -> pathlib.Path:
        """
        Метод валидации пути к файлу
        :param path_to_f: Путь к файлу
        :return: Путь к файлу после валидации
        """
        pass

    @abstractmethod
    def _validate_name(self, f_name: str) -> str:
        """
        Метод валидации имени файла
        :param f_name: Имя файла
        :return: Имя файла после валидации
        """
        pass

    @abstractmethod
    def _write_to_file(self, data: List) -> None:
        """
        Метод для записи вакансий в JSON-файл
        :param data: Данные о вакансии (словарь)
        """
        pass
