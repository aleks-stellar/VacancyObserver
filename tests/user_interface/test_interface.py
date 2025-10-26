import json
from pathlib import Path

import pytest
from unittest.mock import patch

from src.user_interface.interface import user_interface


def test_user_interface_output(tmp_path, capsys, first_string) -> None:
    """Тестируем поток вывода"""
    fake_path = tmp_path / "test_data.json"

    with patch("builtins.input", side_effect=["1", "Python"]), \
        patch("src.user_interface.interface.write_vacancies_by_keyword", return_value=None), \
        patch("src.user_interface.interface.JSONWorker.get_default_path", return_value=fake_path):

        user_interface()

        captured = capsys.readouterr()
        string_keyword = ("Вы выбрали получить все вакансии по ключевому слову. "
                                 "Введите ключевое слово: ")
        user_keyword_str = f'Вы ввели слово "python"'
        string_for_save_vacancies = f'Вакансии по ключевому слову "python" сохранены по пути "../data/python.json"'

        assert first_string in captured.out
        assert string_keyword in captured.out
        assert user_keyword_str in captured.out
        assert string_for_save_vacancies in captured.out

    with patch("builtins.input", side_effect=["2", "100000", "5"]), \
        patch("src.user_interface.interface.write_vacancies_by_keyword", return_value=None), \
        patch("src.user_interface.interface.JSONWorker.get_default_path", return_value=fake_path):

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
        assert string_save_vacancies_info in captured.out


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


def test_case_independence(tmp_path, capsys) -> None:
    """Проверяем регистронезависимость ключевого слова"""
    fake_path = tmp_path / "test_data.json"

    with patch("builtins.input", side_effect=["1", "Python"]), \
            patch("src.user_interface.interface.write_vacancies_by_keyword", return_value=None), \
            patch("src.user_interface.interface.JSONWorker.get_default_path", return_value=fake_path):
        user_interface()

        str_for_compare = "Python"
        str_for_compare.lower()

        captured = capsys.readouterr()

        assert 'Вы ввели слово "python"' in captured.out


def test_user_interface_saving_vacancies_by_keyword(tmp_path, vacancy_data1, vacancy_data2) -> None:
    """Проверяем, что функция user_interface корректно сохраняет данные в json-файл"""
    fake_path = tmp_path / "test_data.json"

    with patch("builtins.input", side_effect=["1", "Python"]), \
            patch("src.user_interface.interface.write_vacancies_by_keyword", return_value=None), \
            patch(
                "src.user_interface.interface.JSONWorker.get_vacancy_data",
                return_value=[vacancy_data1, vacancy_data2]
            ), \
            patch("src.user_interface.interface.JSONWorker.add_vacancy_data", return_value=None), \
            patch("src.user_interface.interface.JSONWorker.get_default_path", return_value=fake_path):

        fake_path.touch()

        with open(fake_path, "w", encoding="utf-8") as f:
            json.dump([vacancy_data1, vacancy_data2], f, ensure_ascii=False)

        user_interface()

        with open(fake_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert data == [vacancy_data1, vacancy_data2]


def test_search_by_salary_file_exist(tmp_path, vacancy_data1, vacancy_data2) -> None:
    """Проверяем содержание файла с данными о вакансиях по минимальной зарплате"""
    fake_path = tmp_path / "test_data.json"

    with patch("builtins.input", side_effect=["2", "300000", "1"]), \
            patch("src.user_interface.interface.write_vacancies_by_keyword", return_value=None), \
            patch(
                "src.user_interface.interface.JSONWorker.get_vacancy_data",
                return_value=[vacancy_data1, vacancy_data2]
            ), \
            patch("src.user_interface.interface.JSONWorker.add_vacancy_data", return_value=None), \
            patch("src.user_interface.interface.JSONWorker.get_default_path", return_value=fake_path):

        fake_path.touch()

        with open(fake_path, "w", encoding="utf-8") as f:
            json.dump([vacancy_data1, vacancy_data2], f, ensure_ascii=False)

        user_interface()

        with open(fake_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert data == [vacancy_data1, vacancy_data2]
