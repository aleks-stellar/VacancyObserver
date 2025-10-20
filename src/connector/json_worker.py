import json
from itertools import count
from multiprocessing.pool import worker

from src.connector.file_worker import FileWorker
import pathlib


class JSONWorker(FileWorker):
    """Класс для работы чтения, записи и удаления информации о вакансиях из JSON-файла"""
    DEFAULT_PATH = pathlib.Path(__file__).parent.parent.parent / "data"
    DEFAULT_NAME = "vacancies.json"

    def __init__(self, path=None, file_name=None):
        """Метод для инициализации"""
        self.__path = self._validate_path(path)
        self.__file_name = self._validate_name(file_name)
        self.__full_path = self.__path / self.__file_name

    def get_vacancy_data(self):
        """Метод для получения данных о вакансиях из JSON-файла"""
        if not self.__full_path.exists() or self.full_path.stat().st_size == 0:
            return []
        with open(self.__full_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    def add_vacancy_data(self, vacancy):
        """Метод для добавления данных о вакансиях в JSON-файл"""
        vacancies = self.get_vacancy_data()
        counter = 0
        for vac in vacancies:
            if vac["alternate_url"] == vacancy["alternate_url"]:
                counter += 1
        if counter == 0:
            vacancies.append(vacancy)
        with open(self.__full_path, "w", encoding="utf-8") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def delete_vacancy_data(self):
        """Метод для удаления данных о вакансиях из JSON-файла"""
        pass

    @property
    def full_path(self):
        return self.__full_path

    def _validate_path(self, path_to_f):
        """Метод валидации пути к файлу"""
        candidate = pathlib.Path(path_to_f) if path_to_f else self.DEFAULT_PATH
        if not candidate.exists():
            candidate.mkdir(parents=True, exist_ok=True)
        return candidate

    def _validate_name(self, f_name):
        """Метод валидации имени файла"""
        if f_name:
            return str(f_name) if str(f_name).endswith(".json") else str(f_name) + ".json"
        return self.DEFAULT_NAME
