from abc import ABC, abstractmethod


class FileWorker(ABC):
    """Абстрактный класс для работы чтения, записи и удаления информации о вакансиях из файла"""

    @abstractmethod
    def get_vacancy_data(self):
        """Метод для получения данных о вакансиях из файла"""
        pass

    @abstractmethod
    def add_vacancy_data(self, vacancy):
        """Метод для добавления данных о вакансиях в файл"""
        pass

    @abstractmethod
    def delete_vacancy_data(self):
        """Метод для удаления данных о вакансиях из файла"""
        pass

    @abstractmethod
    def full_path(self):
        """Метод для чтения полного пути к файлу"""
        pass

    @abstractmethod
    def _validate_path(self, path_to_f):
        """Метод валидации пути к файлу"""
        pass

    @abstractmethod
    def _validate_name(self, f_name):
        """Метод валидации имени файла"""
        pass
