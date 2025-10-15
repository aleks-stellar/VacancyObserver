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


def test_get_title_method() -> None:
    """Проверяем, что метод get_title корректно возвращает защищенный атрибут"""
    vac = BaseVacancy(
        "Python Developer",
        "<https://hh.ru/vacancy/123456>",
        "100 000-150 000 руб.",
        "Требования: опыт работы от 3 лет..."
    )
    assert vac.get_title == "Python Developer"
    assert vac.get_link == "<https://hh.ru/vacancy/123456>"
    assert vac.get_salary == "100 000-150 000 руб."
    assert vac.get_brief_desc == "Требования: опыт работы от 3 лет..."
