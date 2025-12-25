from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class BaseAPI(ABC):
    """Абстрактный класс для работы с API сервисов с вакансиями"""

    @abstractmethod
    def _send_request(
            self,
            text: Optional[str] = None,
            per_page: int = 100,
            page: int = 0,
            salary_from: Optional[int] = None,
    ) -> Dict[str, List[Dict[str, Any]]]:
        """
        Метод отправки POST-запроса на сервер API
        :param text: Ключевое слово
        :param per_page: Количество вакансий за один запрос
        :param page: Номер страницы
        :return: Список вакансий
        """
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, vacancies_amount: int, start_page: int = 0) -> List[Dict[str, Any]]:
        """
        Публичный метод для получения вакансий c HeadHunter
        :param keyword: Ключевое слово
        :param vacancies_amount: Количество вакансий за один запрос
        :param start_page: Номер страницы
        :return: Список вакансий
        """
        pass
