from typing import Any, Dict, List, cast

import requests

from src.api.base_api import BaseAPI
from src.utils.logger_worker import LoggerWorker


class HeadHunterAPI(BaseAPI):
    """Класс для работы с API сервиса HeadHunter"""
    # URL для поиска вакансий на HeadHunter
    __URL = "https://api.hh.ru/vacancies"

    def __init__(self) -> None:
        """Инициализация API и логгера"""
        self.__logger = LoggerWorker()

    def _send_request(self, text: str, per_page: int) -> Dict[str, List[Dict[str, Any]]]:
        """Метод отправки POST-запроса на сервер API"""
        url = self.__URL
        params: Dict[str, Any] = {
            "text": text,
            "per_page": per_page
        }

        self.__logger.info(f"Отправка запроса к {url} с параметрами: {params}")

        response = requests.get(url, params=params)

        if response.status_code != 200:
            self.__logger.error(f"Ошибка запроса: статус {response.status_code}")
            raise ConnectionError("Bad status code")

        self.__logger.info(f"Запрос успешно выполнен, получено {len(response.json().get('items', []))} вакансий")

        # Преобразуем ответ в JSON-формат
        data = response.json()
        return cast(Dict[str, List[Dict[str, Any]]], data)

    def get_vacancies(self, keyword: str, vacancies_amount: int) -> List[Dict[str, Any]]:
        """Публичный метод для получения вакансий c HeadHunter"""
        data = self._send_request(keyword, vacancies_amount)["items"]
        self.__logger.info(f"Получено {len(data)} вакансий по ключевому слову '{keyword}'")
        return data
