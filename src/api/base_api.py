from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseAPI(ABC):
    """Абстрактный класс для работы с API сервисов с вакансиями"""

    @abstractmethod
    def _send_request(self, text: str, per_page: int) -> Dict[str, List[Dict[str, Any]]]:
        """Метод отправки POST-запроса на сервер API"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, vacancies_amount: int) -> List[Dict[str, Any]]:
        """Публичный метод для получения вакансий"""
        pass
