import pytest

from src.vacancy.base_vacancy import BaseVacancy


@pytest.fixture
def vac_1() -> BaseVacancy:
    """Фикстура, возвращающая объект класса BaseVacancy vac_1"""
    return BaseVacancy(
        "Python Developer",
        "<https://hh.ru/vacancy/123456>",
        {"from": 350000, "to": 450000, "currency": "RUB", "gross": False},
        "Требования: опыт работы от 3 лет..."
    )


@pytest.fixture
def vac_2() -> BaseVacancy:
    """Фикстура, возвращающая объект класса BaseVacancy vac_2"""
    return BaseVacancy(
        "Web Developer",
        "<https://hh.ru/vacancy/123457>",
        {"from": 380000, "to": 400000, "currency": "RUB", "gross": False},
        "Требуется опытный веб-разработчик для создания сайта"
    )
