from abc import ABC

import pytest

from src.api.base_api import BaseAPI
from src.api.hh_api import HeadHunterAPI


def test_base_api_is_abstract() -> None:
    """Проверяем, что класс BaseAPI является абстрактным"""
    assert issubclass(BaseAPI, ABC)


def test_base_api_has_abstract_methods() -> None:
    """Проверяем, что у BaseAPI есть абстрактные методы"""
    abstract_methods = BaseAPI.__abstractmethods__
    assert "_send_request" in abstract_methods
    assert "get_vacancies" in abstract_methods


def test_base_api_cannot_be_instantiated() -> None:
    """Проверяем, что нельзя создать экземпляр BaseAPI"""
    with pytest.raises(TypeError):
        BaseAPI()  # type: ignore[abstract]


def test_hh_api_can_be_instantiated() -> None:
    """Проверяем, что HeadHunterAPI реализует абстрактные методы и может быть создан"""
    hh_api = HeadHunterAPI()
    assert hh_api is not None
