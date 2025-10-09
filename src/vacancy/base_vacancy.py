class BaseVacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("title", "link", "salary", "brief_desc")  # title, link, salary, brief_desc

    def __init__(self, title, link, salary, brief_desc):
        """Метод инициализации"""
        pass

    @property
    def get_title(self):
        """Метод для доступа к защищенному атрибуту"""
        pass

    @property
    def get_link(self):
        """Метод для доступа к защищенному атрибуту"""
        pass

    @property
    def get_salary(self):
        """Метод для доступа к защищенному атрибуту"""
        pass

    @property
    def get_brief_desc(self):
        """Метод для доступа к защищенному атрибуту"""
        pass

    def _validate_title(self):
        """Метод валидации названия вакансии"""
        pass

    def _validate_salary(self):
        """Метод валидации зарплаты"""
        pass

    def __gt__(self, other):
        """Метод сравнения"""
        pass

    def __lt__(self, other):
        """Метод сравнения"""
        pass
