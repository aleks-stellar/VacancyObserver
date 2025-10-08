from abc import ABC, abstractmethod


class BaseAPI(ABC):
    """Абстрактный класс для работы с API сервисов с вакансиями"""

    @abstractmethod
    def _send_request(self, keyword, vacancies_amount):
        """Метод отправки POST-запроса на сервер API"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword, vacancies_amount):
        """Публичный метод для получения вакансий"""
        pass
