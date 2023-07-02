from functions import load_students, load_professions, get_student_by_pk, get_profession_by_title, check_fitness


def main():
    """
    Основная функция
    """
    pk = input('Введите номер студента:\n')

    # проверка существует ли ключ 'pk'
    if not pk.isdigit() or not get_student_by_pk(int(pk)):
        quit('У нас нет такого студента')
    else:
        print(f'Студент {get_student_by_pk(int(pk))["full_name"]}\n'
              f'Знает {", ".join(get_student_by_pk(int(pk))["skills"])}')

    title = input(
        f'Выберите специальность для оценки студента {get_student_by_pk(int(pk))["full_name"]}\n').strip().capitalize()

    # проверяем существует ли ключ 'title'
    if get_profession_by_title(title) is None:
        quit('У нас нет такой специальности')

    # записываем функции в переменные для упрощения чтения кода дальше
    student, profession = get_student_by_pk(int(pk)), get_profession_by_title(title)
    check = check_fitness(student, profession)

    # выводим насколько студент подходит по профессии
    print(
        f'Пригодность {str(check["fit_percent"])}%\n'
        f'{student["full_name"]} знает {", ".join(check["has"])}\n'
        f'{student["full_name"]} не знает {", ".join(check["lacks"])}')


if __name__ == '__main__':
    main()
