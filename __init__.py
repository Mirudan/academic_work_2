from functions import *


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
    get_profession_by_title(title)

    # записываем функции в переменные для упрощения чтения кода дальше
    student, profession = get_student_by_pk(int(pk)), get_profession_by_title(title)

    # выводим насколько студент подходит по профессии
    print(
        f'Пригодность {check_fitness(student, profession)["fit_percent"]}\n'
        f'{student["full_name"]} знает {check_fitness(student, profession)["has"]}\n'
        f'{student["full_name"]} не знает {check_fitness(student, profession)["lacks"]}')


if __name__ == '__main__':
    main()
