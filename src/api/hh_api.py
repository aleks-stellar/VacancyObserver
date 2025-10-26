from typing import Any, Dict, List, cast, Optional

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

    def _send_request(
            self,
            text: Optional[str] = None,
            per_page: int = 100,
            page: int = 0,
            salary_from: Optional[int] = None,
    ) -> Dict[str, List[Dict[str, Any]]]:
        """
        :param text: Ключевое слово для поиска
        :param per_page: Количество вакансий за один запрос
        :param page: Номер страницы
        :param salary_from: Минимальная зарплата
        :return: Ответ API в виде словаря
        """
        params: Dict[str, Any] = {"per_page": per_page, "page": page}

        if text:
            params["text"] = text
        if salary_from:
            params["salary_from"] = salary_from

        self.__logger.info(f"Отправка запроса к {self.__URL} с параметрами: {params}")

        response = requests.get(self.__URL, params=params)

        if response.status_code != 200:
            self.__logger.error(f"Ошибка запроса: статус {response.status_code}")
            raise ConnectionError("Bad status code")

        self.__logger.info(f"Запрос успешно выполнен, получено {len(response.json().get('items', []))} вакансий")

        # Преобразуем ответ в JSON-формат
        data = response.json()
        return cast(Dict[str, List[Dict[str, Any]]], data)

    def get_vacancies(
            self,
            keyword: Optional[str] = None,
            vacancies_amount: int = 100,
            start_page: int = 0,
            salary_from: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """
        Публичный метод для получения вакансий c HeadHunter
        :param keyword:Ключевое слово для поиска
        :param vacancies_amount: Количество вакансий за один запрос
        :param start_page: Номер страницы
        :param salary_from: Минимальная зарплата
        """
        data = self._send_request(
            text=keyword,
            per_page=vacancies_amount,
            page=start_page,
            salary_from=salary_from,
        )["items"]
        self.__logger.info(f"Получено {len(data)} вакансий по ключевому слову '{keyword}'")
        return data
