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
