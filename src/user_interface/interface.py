def user_interface() -> None:
    """Функция для взаимодействия пользователя с приложением"""
    first_str = ('Введите "1", если хотите получить все вакансии по ключевому слову и "2", '
                    'если хотите получить топ N вакансий по минимальной зарплате')

    print(first_str)

    try:
        operation_choice = int(input("Введите число: "))
    except ValueError:
        raise ValueError('Необходимо ввести число "1" или "2"')

    if operation_choice == 1:
        print(f"Вы выбрали получить все вакансии по ключевому слову. "
              "Введите ключевое слово: ", end="")

        user_keyword = input()
        string_user_keyword = f'Вы ввели слово "{user_keyword}"'
        print(string_user_keyword)

    if operation_choice == 2:
        print(f"Вы выбрали получить топ N вакансий по минимальной зарплате. "
              "Введите минимальную зарплату: ", end="")

        try:
            user_min_salary = int(input())
            string_min_salary = f"Вы ввели минимальную зарплату {user_min_salary}"
            print(string_min_salary)
        except ValueError:
            raise ValueError('Необходимо ввести целое число')

        print(f"Введите число N: ", end="")

        try:
            user_n_for_top = int(input())
            string_n_for_top = f"Вы ввели число N = {user_n_for_top}"
            print(string_n_for_top)
        except ValueError:
            raise ValueError('Необходимо ввести целое число')


if __name__ == '__main__':
    user_interface()
