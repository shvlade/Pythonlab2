# -*- coding: utf8 -*-
import csv


def get_top_students(students, n):
    """
    Возвращает список из n студентов с наивысшим средним баллом.
    """
    top_students = sorted(students, key=lambda x: x['Средний балл'], reverse=True)[:n]
    return top_students


def get_average_age(students):
    """
    Возвращает средний возраст студентов.
    """
    total_age = sum(student['Возраст'] for student in students)
    average_age = total_age / len(students)
    return average_age


def filter_students_by_grade(students, min_grade):
    """
    Возвращает список студентов с средним баллом выше min_grade.
    """
    filtered = [student for student in students if student['Средний балл'] > min_grade]
    return filtered


def read_students(filename):
    """
    Читает данные студентов из CSV-файла и преобразует в список словарей.
    """
    students = []
    with open(filename, 'r', encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            student = {
                'Имя': row['Имя'],
                'Возраст': int(row['Возраст']),
                'Средний балл': float(row['Средний балл'])
            }
            students.append(student)
    return students


def write_report(filename, content):
    """
    Сохраняет строку отчета в текстовый файл.
    """
    with open(filename, 'w', encoding='cp1251') as file:
        file.write(content)


# Основной блок выполнения

if __name__ == "__main__":
    # 1. Чтение студентов из файла
    students = read_students('students.csv')

    # 2. Получение топ-2 студентов по среднему баллу
    top_students = get_top_students(students, 2)

    # 3. Вычисление среднего возраста
    average_age = get_average_age(students)

    # 4. Фильтрация студентов с баллом выше 4.0
    filtered_students = filter_students_by_grade(students, 4.0)

    # 5. Сортировка студентов по возрасту с использованием лямбда-функции
    sorted_by_age = sorted(students, key=lambda x: x['Возраст'])

    # 6. Формирование текста отчета
    report_content = " Отчет о студентах \n\n"

    report_content += "Топ 2 студента по среднему баллу:\n"
    for student in top_students:
        report_content += f"{student['Имя']} - {student['Средний балл']}\n"

    report_content += f"\nСредний возраст студентов: {average_age:.2f}\n\n"

    report_content += "Студенты с баллом выше 4.0:\n"
    for student in filtered_students:
        report_content += f"{student['Имя']} - {student['Средний балл']}\n"

    report_content += "\nСтуденты, отсортированные по возрасту:\n"
    for student in sorted_by_age:
        report_content += f"{student['Имя']} - {student['Возраст']} лет\n"

    # 7. Сохранение отчета в файл
    write_report('report.txt', report_content)

    print("Отчет успешно создан в файле report.txt")