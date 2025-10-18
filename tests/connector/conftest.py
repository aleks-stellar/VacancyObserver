from typing import Dict

import pytest


@pytest.fixture
def vacancy_data1() -> Dict[str, str | Dict]:
    """Фикстура с данными о вакансии"""
    return {
        "name": "Python Developer",
        "alternate_url": "<https://hh.ru/vacancy/123456>",
        "salary": {"from": 350000, "to": 450000, "currency": "RUB", "gross": False},
        "requirement": "Требования: опыт работы от 3 лет..."
    }


@pytest.fixture
def vacancy_data2() -> Dict[str, str | Dict]:
    """Фикстура с данными о вакансии"""
    return {
        "name": "Web Developer",
        "alternate_url": "<https://hh.ru/vacancy/123457>",
        "salary": {"from": 250000, "to": 400000, "currency": "RUB", "gross": False},
        "requirement": "Требования: опыт работы от 5 лет..."
    }
