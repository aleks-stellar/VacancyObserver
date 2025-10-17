class BaseVacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("_title", "_link", "_salary", "_brief_desc")

    def __init__(self, title, link, salary, brief_desc):
        """Метод инициализации"""
        self._title = self._validate_title(title)
        self._link = link
        self._salary = self._validate_salary(salary)
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

    @staticmethod
    def _validate_title(headline):
        """Метод валидации названия вакансии"""
        if not headline.strip():
            return "Название не указано"
        return headline

    @staticmethod
    def _validate_salary(wage):
        """Метод валидации зарплаты"""
        if not wage:
            return 0
        return wage

    def __gt__(self, other):
        """Метод сравнения"""
        if not isinstance(other, BaseVacancy):
            raise TypeError("Можно сравнивать только объекты класса BaseVacancy")
        self_avg_salary = (self.salary["from"] + self.salary["to"]) / 2
        other_avg_salary = (other.salary["from"] + other.salary["to"]) / 2
        return self_avg_salary > other_avg_salary

    def __lt__(self, other):
        """Метод сравнения"""
        if not isinstance(other, BaseVacancy):
            raise TypeError("Можно сравнивать только объекты класса BaseVacancy")
        self_avg_salary = (self.salary["from"] + self.salary["to"]) / 2
        other_avg_salary = (other.salary["from"] + other.salary["to"]) / 2
        return self_avg_salary < other_avg_salary

    def __eq__(self, other):
        """Метод сравнения"""
        if not isinstance(other, BaseVacancy):
            raise TypeError("Можно сравнивать только объекты класса BaseVacancy")
        self_avg_salary = (self.salary["from"] + self.salary["to"]) / 2
        other_avg_salary = (other.salary["from"] + other.salary["to"]) / 2
        return self_avg_salary == other_avg_salary
