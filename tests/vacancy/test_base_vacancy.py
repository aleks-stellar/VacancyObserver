import inspect

import pytest

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


def test_get_title_method(vac_1: BaseVacancy) -> None:
    """Проверяем, что метод get_title корректно возвращает защищенный атрибут"""
    assert vac_1.title == "Python Developer"
    assert vac_1.link == "<https://hh.ru/vacancy/123456>"
    assert vac_1.salary == {"from": 350000, "to": 450000, "currency": "RUB", "gross": False}
    assert vac_1.brief_desc == "Требования: опыт работы от 3 лет..."


def test_comparison_methods_is_magic() -> None:
    """Проверяем, что методы сравнения магические"""
    assert hasattr(BaseVacancy, "__gt__"), "Метод __gt__ не реализован"
    assert hasattr(BaseVacancy, "__lt__"), "Метод __lt__ не реализован"


def test_gt_method_is_implement(vac_1: BaseVacancy, vac_2: BaseVacancy) -> None:
    """Проверяем, что в классе реализован метод сравнения вакансий по зарплате (__gt__)"""
    assert vac_1 > vac_2
    assert not vac_2 > vac_1


def test_lt_method_is_implement(vac_1: BaseVacancy, vac_2: BaseVacancy) -> None:
    """Проверяем, что в классе реализован метод сравнения вакансий по зарплате (__lt__)"""
    assert vac_2 < vac_1
    assert not vac_1 < vac_2


def test_eq_method_is_implement(vac_1: BaseVacancy, vac_2: BaseVacancy) -> None:
    """Проверяем, что в классе реализован метод сравнения вакансий по зарплате (__eq__)"""
    assert not vac_1 == vac_2


def test_gt_method_with_not_base_vacancy_object(vac_1: BaseVacancy) -> None:
    """Проверяем, что метод сравнения выдаст ошибку TypeError при попытке сравнить не с объектом класса BaseVacancy"""
    with pytest.raises(TypeError) as e:
        _ = vac_1 > 100000.0
    assert str(e.value) == "Можно сравнивать только объекты класса BaseVacancy"


def test_lt_method_with_not_base_vacancy_object(vac_1: BaseVacancy) -> None:
    """Проверяем, что метод сравнения выдаст ошибку TypeError при попытке сравнить не с объектом класса BaseVacancy"""
    with pytest.raises(TypeError) as e:
        _ = not vac_1 < 100000.0
    assert str(e.value) == "Можно сравнивать только объекты класса BaseVacancy"


def test_eq_method_with_not_base_vacancy_object(vac_1: BaseVacancy) -> None:
    """Проверяем, что метод сравнения выдаст ошибку TypeError при попытке сравнить не с объектом класса BaseVacancy"""
    with pytest.raises(TypeError) as e:
        _ = not vac_1 == 100000.0
    assert str(e.value) == "Можно сравнивать только объекты класса BaseVacancy"


def test_validation_title_during_init() -> None:
    """Проверяем, что при инициализации объекта происходит валидация по названию"""
    vacancy = BaseVacancy("", "", {
        "from": 380000, "to": 400000, "currency": "RUB", "gross": False
    }, "")

    assert vacancy.title == "Название не указано"

    vacancy = BaseVacancy("  ", "", {
        "from": 380000, "to": 400000, "currency": "RUB", "gross": False
    }, "")

    assert vacancy.title == "Название не указано"


def test_validation_salary_during_init() -> None:
    """Проверяем, что при инициализации объекта происходит валидация по зарплате"""
    vacancy = BaseVacancy("", "", {}, "")
    assert vacancy.salary == {"from": 0, "to": 0, "currency": "", "gross": False}
