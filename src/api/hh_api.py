import requests
import json
from src.api.base_api import BaseAPI


class HeadHunterAPI(BaseAPI):
    """Класс для работы с API сервиса HeadHunter"""
    # URL для поиска вакансий на HeadHunter
    __URL = "https://api.hh.ru/vacancies"

    def __init__(self):
        """Метод инициализации"""
        pass

    def _send_request(self):
        """Метод отправки POST-запроса на сервер API"""
        url = self.__URL
        response = requests.get(url)

        if response.status_code != 200:
            raise ConnectionError("Bad status code")

        # Преобразуем ответ в JSON-формат
        data = response.json()
        return data

    def _process_response(self):
        """Метод обработки GET-ответа"""

    def get_vacancies(self):
        """Публичный метод для получения вакансий c HeadHunter"""
        return self._send_request()
