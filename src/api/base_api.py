from abc import ABC, abstractmethod


class BaseAPI(ABC):
    """Абстрактный класс для работы с API сервисов с вакансиями"""

    @abstractmethod
    def send_request(self):
        """Метод отправки POST-запроса на сервер API"""
        pass

    @abstractmethod
    def process_response(self):
        """Метод обработки GET-ответа"""
        pass
