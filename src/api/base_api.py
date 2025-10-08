from abc import ABC, abstractmethod


class BaseAPI(ABC):
    """Абстрактный класс для работы с API сервисов с вакансиями"""

    @abstractmethod
    def _send_request(self, text: str, per_page: int):
        """Метод отправки POST-запроса на сервер API"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, vacancies_amount: int):
        """Публичный метод для получения вакансий"""
        pass
