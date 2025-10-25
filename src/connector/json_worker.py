import json
import pathlib
from typing import Dict, List, Optional

from src.connector.file_worker import FileWorker
from src.utils.logger_worker import LoggerWorker


class JSONWorker(FileWorker):
    """Класс для работы чтения, записи и удаления информации о вакансиях из JSON-файла"""
    __DEFAULT_PATH = pathlib.Path(__file__).parent.parent.parent / "data"
    __DEFAULT_NAME = "vacancies.json"
    __LINK_FOR_VACANCY = "https://hh.ru/vacancy/"

    def __init__(self, path: Optional[str] = None, file_name: Optional[str] = None) -> None:
        """
        Метод для инициализации
        :param path: Путь к файлу
        :param file_name: Имя файла
        """
        self.__path: pathlib.Path = self._validate_path(path)
        self.__file_name: str = self._validate_name(file_name)
        self.__full_path: pathlib.Path = self.__path / self.__file_name
        self.logger: LoggerWorker = LoggerWorker()

    def get_vacancy_data(self, path: pathlib.Path = None) -> List[Dict]:
        """Метод для получения данных о вакансиях из JSON-файла"""
        if not path:
            if not self.__full_path.exists() or self.full_path.stat().st_size == 0:
                return []
            with open(self.__full_path, "r", encoding="utf-8") as f:
                data: List[Dict] = json.load(f)
            return data
        if path:
            if not path.exists() or self.full_path.stat().st_size == 0:
                return []
            with open(path, "r", encoding="utf-8") as f:
                data: List[Dict] = json.load(f)
            return data

    def add_vacancy_data(self, vacancy: Dict) -> None:
        """
        Метод для добавления данных о вакансиях в файл
        :param vacancy: Словарь с данными о вакансии
        """
        vacancies: List[Dict] = self.get_vacancy_data()
        if not any(vac["alternate_url"] == vacancy["alternate_url"] for vac in vacancies):
            vacancies.append(vacancy)
            self.logger.info(f"Добавлена новая вакансия: {vacancy['name']}")
        self._write_to_file(vacancies)

    def delete_vacancy_data(self, vacancy_id: int) -> None:
        """
        Метод для удаления данных о вакансиях из файла
        :param vacancy_id: ID вакансии
        """
        data: List[Dict] = self.get_vacancy_data()
        link = self.__LINK_FOR_VACANCY + str(vacancy_id)
        data_without_vacancy: List[Dict] = []
        vacancy_was_deleted: Optional[Dict] = None

        for vac in data:
            if vac["alternate_url"] != link:
                data_without_vacancy.append(vac)
            else:
                vacancy_was_deleted = vac

        self._write_to_file(data_without_vacancy)

        if vacancy_was_deleted:
            self.logger.info(f"Удалена вакансия: {vacancy_was_deleted['name']}")
        else:
            self.logger.warning(f"Попытка удалить несуществующую вакансию с ID {vacancy_id}")

    @property
    def full_path(self) -> pathlib.Path:
        return self.__full_path

    def _validate_path(self, path_to_f: Optional[str]) -> pathlib.Path:
        """
                Метод валидации пути к файлу
                :param path_to_f: Путь к файлу
                :return: Путь к файлу после валидации
                """
        candidate: pathlib.Path = pathlib.Path(path_to_f) if path_to_f else self.__DEFAULT_PATH
        if not candidate.exists():
            candidate.mkdir(parents=True, exist_ok=True)
        return candidate

    def _validate_name(self, f_name: Optional[str]) -> str:
        """
        Метод валидации имени файла
        :param f_name: Имя файла
        :return: Имя файла после валидации
        """
        if f_name:
            return str(f_name) if str(f_name).endswith(".json") else str(f_name) + ".json"
        return self.__DEFAULT_NAME

    def _write_to_file(self, data: List[Dict]) -> None:
        """
        Метод для записи вакансий в JSON-файл
        :param data: Данные о вакансии (словарь)
        """
        with open(self.__full_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
