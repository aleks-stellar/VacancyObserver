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

    def _send_request(self, text, per_page):
        """Метод отправки POST-запроса на сервер API"""
        url = self.__URL

        params = {
            "text": text,
            "per_page": per_page
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            raise ConnectionError("Bad status code")

        # Преобразуем ответ в JSON-формат
        data = response.json()
        return data

    def get_vacancies(self, keyword, vacancies_amount):
        """Публичный метод для получения вакансий c HeadHunter"""
        return self._send_request(keyword, vacancies_amount)
