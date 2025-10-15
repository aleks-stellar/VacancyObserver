class BaseVacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("_title", "_link", "_salary", "_brief_desc")

    def __init__(self, title, link, salary, brief_desc):
        """Метод инициализации"""
        self._title = title
        self._link = link
        self._salary = salary
        self._brief_desc = brief_desc

    @property
    def title(self):
        """Метод для доступа к защищенному атрибуту"""
        return self._title

    @property
    def link(self):
        """Метод для доступа к защищенному атрибуту"""
        return self._link

    @property
    def salary(self):
        """Метод для доступа к защищенному атрибуту"""
        return self._salary

    @property
    def brief_desc(self):
        """Метод для доступа к защищенному атрибуту"""
        return self._brief_desc

    def _validate_title(self):
        """Метод валидации названия вакансии"""
        pass

    def _validate_salary(self):
        """Метод валидации зарплаты"""
        pass

    def __gt__(self, other):
        """Метод сравнения"""
        return self.get_salary

    def __lt__(self, other):
        """Метод сравнения"""
        pass
