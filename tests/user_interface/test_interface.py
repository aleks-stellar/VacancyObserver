import pytest
from unittest.mock import patch

from src.user_interface.interface import user_interface


def test_user_interface_output(capsys, first_string) -> None:
    """Тестируем поток вывода"""
    with patch("builtins.input", side_effect=["1", "Python", "нет"]):
        user_interface()

        captured = capsys.readouterr()
        string_keyword = ("Вы выбрали получить все вакансии по ключевому слову. "
                                 "Введите ключевое слово: ")
        user_keyword_str = f'Вы ввели слово "python"'
        string_for_save_vacancies = f'Вакансии по ключевому слову "python" сохранены по пути "../data/python.json"'

        next_step_string = "Хотите получить топ N вакансий по минимальной зарплате? да/нет: "

        assert first_string in captured.out
        assert string_keyword in captured.out
        assert user_keyword_str in captured.out
        assert string_for_save_vacancies in captured.out
        assert next_step_string in captured.out

    with patch("builtins.input", side_effect=["2", "100000", "5"]):
        user_interface()

        captured = capsys.readouterr()
        string_min_salary = ("Вы выбрали получить топ N вакансий по минимальной зарплате. "
                                    "Введите минимальную зарплату: ")
        string_min_salary_str = f"Вы ввели минимальную зарплату 100000"
        string_n_for_top_str = f"Вы ввели число N = 5"

        string_save_vacancies_info = (f'Топ 5 вакансий по минимальной зарплате 100000 руб. '
                               f'сохранены по пути "../data/top_5_salary_100000.json"')


        assert first_string in captured.out
        assert string_min_salary in captured.out
        assert string_min_salary_str in captured.out
        assert string_n_for_top_str in captured.out
        assert  string_save_vacancies_info in captured.out


def test_invalid_input() -> None:
    """Проверяем поведение функции при некорректных входных данных"""
    with pytest.raises(ValueError) as exc_info:
        with patch("builtins.input", return_value="one"):
            user_interface()

    assert str(exc_info.value) == 'Необходимо ввести число "1" или "2"'

    with pytest.raises(ValueError) as exc_info:
        with patch("builtins.input", side_effect=["2", "one million dollars"]):
            user_interface()

    assert str(exc_info.value) == 'Необходимо ввести целое число'

    with pytest.raises(ValueError) as exc_info:
        with patch("builtins.input", side_effect=["2", "100000", "top five"]):
            user_interface()

    assert str(exc_info.value) == 'Необходимо ввести целое число'


def test_case_independence(capsys) -> None:
    """Проверяем регистронезависимость ключевого слова"""
    with patch("builtins.input", side_effect=["1", "Python", "Нет"]):
        user_interface()

        str_for_compare = "Python"
        str_for_compare.lower()

        captured = capsys.readouterr()

        assert 'Вы ввели слово "python"' in captured.out
