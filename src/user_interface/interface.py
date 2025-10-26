from src.connector.json_worker import JSONWorker
from src.vacancy.base_vacancy import BaseVacancy
from src.api.hh_api import HeadHunterAPI
from src.utils.vacancy_getter import write_vacancies_by_keyword, write_top_vacancies_by_salary


def user_interface() -> None:
    """Функция для взаимодействия пользователя с приложением"""
    print(
        'Введите "1", если хотите получить все вакансии по ключевому слову и "2", '
        'если хотите получить топ N вакансий по минимальной зарплате'
    )

    try:
        operation_choice = int(input("Введите число: "))
    except ValueError:
        raise ValueError('Необходимо ввести число "1" или "2"')

    json_saver = JSONWorker()
    path_to_data_file = json_saver.get_default_path()

    if operation_choice == 1:
        print(
            f"Вы выбрали получить все вакансии по ключевому слову. "
            "Введите ключевое слово: ",
            end=""
        )
        user_keyword = input().strip().lower()
        print(f'Вы ввели слово "{user_keyword}"')

        # Сохраняем вакансии по ключевому слову
        write_vacancies_by_keyword(keyword=user_keyword, path=path_to_data_file)
        print(
            f'Вакансии по ключевому слову "{user_keyword}" '
            f'сохранены по пути "../data/{user_keyword}.json"'
        )

    elif operation_choice == 2:
        # Ввод минимальной зарплаты
        print(f"Вы выбрали получить топ N вакансий по минимальной зарплате. "
              "Введите минимальную зарплату: ", end="")
        try:
            user_min_salary = int(input())
            if user_min_salary <= 0:
                raise ValueError
            print(f"Вы ввели минимальную зарплату {user_min_salary}")
        except ValueError:
            raise ValueError('Необходимо ввести положительное целое число')

        # Ввод числа N
        print("Введите число N: ", end="")
        try:
            user_n_for_top = int(input())
            if user_n_for_top <= 0:
                raise ValueError
            print(f"Вы ввели число N = {user_n_for_top}")
        except ValueError:
            raise ValueError('Необходимо ввести положительное целое число')

        # Сохраняем топ вакансий по зарплате
        write_top_vacancies_by_salary(
            min_salary=user_min_salary,
            top_number=user_n_for_top,
            path=path_to_data_file
        )
        print(
            f'Топ {user_n_for_top} вакансий по минимальной зарплате {user_min_salary} руб. '
            f'сохранены по пути "../data/top_{user_n_for_top}_salary_{user_min_salary}.json"'
        )

    else:
        raise ValueError('Необходимо ввести число "1" или "2"')


if __name__ == '__main__':
    user_interface()
