import json

students_file = 'students.json'
professions_file = 'professions.json'


def load_students(students_file):
    """
    Загружает список студентов из файла
    """
    with open(students_file, encoding='utf-8') as file:
        students_json = file.read()

    profiles_list = json.loads(students_json)
    return profiles_list


def load_professions(professions_file):
    """
    Загружает список профессий из файла
    """
    with open(professions_file, encoding='utf-8') as file:
        professions_json = file.read()

    profiles_list = json.loads(professions_json)

    return profiles_list


def get_student_by_pk(pk):
    """
    Получает словарь с данными студента по его pk
    """
    for student in load_students(students_file):
        if pk == student['pk']:
            return student


def get_profession_by_title(title):
    """
    Получает словарь с инфо о профе по названию
    """
    for title_dict in load_professions(professions_file):
        if title == title_dict['title']:
            return title_dict['skills']


def check_fitness(student, profession):
    """
    Проверяет что есть в стэке и чего не хватает для профы
    """
    stud_skills = set(student["skills"])
    prof_skills = set(profession)

    has = list(stud_skills & prof_skills)
    lacks = list(prof_skills.difference(stud_skills))
    check_percent = round(len(has) / len(profession) * 100)

    check_dict = {
        "has": has,
        "lacks": lacks,
        "fit_percent": check_percent
    }
    return check_dict
