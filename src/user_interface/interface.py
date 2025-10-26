from src.connector.json_worker import JSONWorker
from src.vacancy.base_vacancy import BaseVacancy
from src.api.hh_api import HeadHunterAPI
from src.utils.vacancy_getter import write_vacancies_by_keyword


def user_interface() -> None:
    """Функция для взаимодействия пользователя с приложением"""
    print(('Введите "1", если хотите получить все вакансии по ключевому слову и "2", '
           'если хотите получить топ N вакансий по минимальной зарплате'))

    try:
        operation_choice = int(input("Введите число: "))
    except ValueError:
        raise ValueError('Необходимо ввести число "1" или "2"')

    if operation_choice == 1:
        print(f"Вы выбрали получить все вакансии по ключевому слову. "
              "Введите ключевое слово: ", end="")

        user_keyword = input().lower()
        print(f'Вы ввели слово "{user_keyword}"')

        json_saver = JSONWorker()
        path_to_data_file = json_saver.get_default_path()
        write_vacancies_by_keyword(keyword=user_keyword, path=path_to_data_file)
        vacancy_list = json_saver.get_vacancy_data(path=path_to_data_file)

        for vacancy in vacancy_list:
            json_saver.add_vacancy_data(vacancy=vacancy)

        print(f'Вакансии по ключевому слову '
              f'"{user_keyword}" сохранены по пути "../data/{user_keyword}.json"')

    if operation_choice == 2:
        print(f"Вы выбрали получить топ N вакансий по минимальной зарплате. "
              "Введите минимальную зарплату: ", end="")

        try:
            user_min_salary = int(input())
            print(f"Вы ввели минимальную зарплату {user_min_salary}")
        except ValueError:
            raise ValueError('Необходимо ввести целое число')

        print(f"Введите число N: ", end="")

        try:
            user_n_for_top = int(input())
            print(f"Вы ввели число N = {user_n_for_top}")
        except ValueError:
            raise ValueError('Необходимо ввести целое число')

        print((f'Топ {user_n_for_top} вакансий по минимальной зарплате {user_min_salary} руб. '
               f'сохранены по пути "../data/top_{user_n_for_top}_salary_{user_min_salary}.json"'))


if __name__ == '__main__':
    user_interface()
