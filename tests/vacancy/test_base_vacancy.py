import inspect

from src.vacancy.base_vacancy import BaseVacancy


def test_base_vacancy_has_slots() -> None:
    """Проверяем, что в классе BaseVacancy используется __slots__"""
    assert hasattr(BaseVacancy, "__slots__"), "В классе BaseVacancy отсутствует __slots__"
    slots = getattr(BaseVacancy, "__slots__")
    assert isinstance(slots, (tuple, list)), "__slots__ должен быть списком или кортежем"
    assert len(slots) > 0, "__slots__ должен содержать атрибуты"


def test_vacancy_init_requires_four_arguments() -> None:
    """Проверяем, что при инициализации объекта класса BaseVacancy требуется минимум 4 аргумента"""
    sig = inspect.signature(BaseVacancy.__init__)
    params_amount = len(sig.parameters) - 1
    assert params_amount >= 4


def test_get_title_method(vac_1) -> None:
    """Проверяем, что метод get_title корректно возвращает защищенный атрибут"""
    assert vac_1.get_title == "Python Developer"
    assert vac_1.get_link == "<https://hh.ru/vacancy/123456>"
    assert vac_1.get_salary == {"from": 350000, "to": 450000, "currency": "RUR", "gross": False}
    assert vac_1.get_brief_desc == "Требования: опыт работы от 3 лет..."


def test_comparison_methods_is_magic() -> None:
    """Проверяем, что методы сравнения магические"""
    assert hasattr(BaseVacancy, "__gt__"), "Метод __gt__ не реализован"
    assert hasattr(BaseVacancy, "__lt__"), "Метод __lt__ не реализован"


def test_comparison_methods_is_implement() -> None:
    """Проверяем, что в классе реализованы методы сравнения вакансий по зарплате"""
