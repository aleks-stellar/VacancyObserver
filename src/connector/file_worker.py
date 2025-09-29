from abc import ABC, abstractmethod


class FileWorker(ABC):
    """Абстрактный класс для работы чтения, записи и удаления информации о вакансиях из файла"""

    @abstractmethod
    def get_vacancy_data(self):
        """Метод для получения данных о вакансиях из файла"""
        pass

    @abstractmethod
    def add_vacancy_data(self):
        """Метод для добавления данных о вакансиях в файл"""
        pass

    @abstractmethod
    def delete_vacancy_data(self):
        """Метод для удаления данных о вакансиях из файла"""
        pass
