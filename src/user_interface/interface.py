from src.connector.json_worker import JSONWorker
from src.vacancy.base_vacancy import BaseVacancy


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

        print(f'Вакансии по ключевому слову '
                               f'"{user_keyword}" сохранены по пути "../data/{user_keyword}.json"')

        print(f"Хотите получить топ N вакансий по минимальной зарплате? да/нет: ", end="")

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
