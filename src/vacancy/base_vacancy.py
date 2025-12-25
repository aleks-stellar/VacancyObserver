from typing import Any, Dict, Union

from src.utils.logger_worker import LoggerWorker


class BaseVacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("_title", "_link", "_salary", "_brief_desc", "_logger")

    def __init__(self, title: str, link: str, salary: Dict[str, Union[str, int, bool]], brief_desc: str) -> None:
        """
        Метод инициализации
        :param title: Название вакансии
        :param link: Ссылка на вакансию
        :param salary: Зарплата (словарь)
        :param brief_desc: Краткое описание вакансии (требования)
        """
        self._title = self._validate_title(title)
        self._link = link
        self._salary = self._validate_salary(salary)
        self._brief_desc = brief_desc

        # Инициализация логгера
        self._logger = LoggerWorker()
        self.logger.info(f"Создана вакансия: {self._title}")

    @property
    def logger(self) -> LoggerWorker:
        """Возвращает экземпляр логгера"""
        return self._logger

    @property
    def title(self) -> str:
        """Метод для доступа к защищенному атрибуту"""
        return self._title

    @property
    def link(self) -> str:
        """Метод для доступа к защищенному атрибуту"""
        return self._link

    @property
    def salary(self) -> Dict[str, Union[str, int, bool]]:
        """Метод для доступа к защищенному атрибуту"""
        return self._salary

    @property
    def brief_desc(self) -> str:
        """Метод для доступа к защищенному атрибуту"""
        return self._brief_desc

    @staticmethod
    def _validate_title(headline: str) -> str:
        """Метод валидации названия вакансии"""
        if not headline.strip():
            return "Название не указано"
        return headline

    @staticmethod
    def _validate_salary(wage: Dict[str, Union[str, int, bool]]) -> Dict[str, Union[str, int, bool]]:
        """
        Метод валидации зарплаты
        :param wage: Зарплата (словарь)
        :return: Зарплата (словарь)
        """
        if not wage:
            return {"from": 0, "to": 0, "currency": "", "gross": False}
        return wage

    def get_vacancy(self) -> Dict[str, Any]:
        """Метод для получения вакансий в формате, соответствующем атрибутам класса"""
        return {
            "name": self.title,
            "alternate_url": self.link,
            "salary": self.salary,
            "requirement": self.brief_desc
        }

    def __gt__(self, other: object) -> bool:
        """Метод сравнения"""
        if not isinstance(other, BaseVacancy):
            raise TypeError("Можно сравнивать только объекты класса BaseVacancy")
        self_avg_salary = (float(self.salary["from"]) + float(self.salary["to"])) / 2
        other_avg_salary = (float(other.salary["from"]) + float(other.salary["to"])) / 2
        return self_avg_salary > other_avg_salary

    def __lt__(self, other: object) -> bool:
        """Метод сравнения"""
        if not isinstance(other, BaseVacancy):
            raise TypeError("Можно сравнивать только объекты класса BaseVacancy")
        self_avg_salary = (float(self.salary["from"]) + float(self.salary["to"])) / 2
        other_avg_salary = (float(other.salary["from"]) + float(other.salary["to"])) / 2
        return self_avg_salary < other_avg_salary

    def __eq__(self, other: object) -> bool:
        """Метод сравнения"""
        if not isinstance(other, BaseVacancy):
            raise TypeError("Можно сравнивать только объекты класса BaseVacancy")
        self_avg_salary = (float(self.salary["from"]) + float(self.salary["to"])) / 2
        other_avg_salary = (float(other.salary["from"]) + float(other.salary["to"])) / 2
        return self_avg_salary == other_avg_salary
