from abc import ABC, abstractmethod


class BaseAPI(ABC):
    """Абстрактный класс для работы с API сервисов с вакансиями."""

    @abstractmethod
    def send_request(self):
        pass

    @abstractmethod
    def process_response(self):
        pass
