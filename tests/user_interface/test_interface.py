import pytest
from unittest.mock import patch

from src.user_interface.interface import user_interface


def test_user_interface_output(capsys, first_string) -> None:
    """Тестируем поток вывода"""
    with patch("builtins.input", return_value="1"):
        user_interface()

        captured = capsys.readouterr()
        second_string_keyword = ("Вы выбрали получить все вакансии по ключевому слову. "
                                 "Введите ключевое слово: ")

        assert first_string in captured.out
        assert second_string_keyword in captured.out

    with patch("builtins.input", return_value="2"):
        user_interface()

        captured = capsys.readouterr()
        second_string_min_salary = ("Вы выбрали получить топ вакансий по минимальной зарплате. "
                                    "Введите минимальную зарплату: ")

        assert first_string in captured.out
        assert second_string_min_salary in captured.out


def test_invalid_input() -> None:
    """Проверяем поведение функции при некорректных входных данных"""
    with pytest.raises(ValueError) as exc_info:
        with patch("builtins.input", return_value="one"):
            user_interface()

    assert str(exc_info.value) == 'Необходимо ввести число "1" или "2"'


def test_user_interface_input(capsys) -> None:
    """Тестируем поток ввода"""
    with patch("builtins.input", return_value="1"):

        user_interface()



