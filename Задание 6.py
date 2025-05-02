# -*- coding: utf8 -*-
import re


# 1. Чтение текстового файла и поиск дат 
def read_and_find_dates(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    # Регулярное выражение для поиска дат
    pattern = r'\b\d{2}\.\d{2}\.\d{4}\b'
    dates = re.findall(pattern, text)
    return dates


# 2. Преобразование дат в формат YYYY-MM-DD
def convert_date_format(dates):
    converted = []
    for date in dates:
        day, month, year = date.split('.')
        new_format = f"{year}-{month}-{day}"
        converted.append(new_format)
    return converted


# 3. Сохранение дат в файл
def save_dates_to_file(dates, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for date in dates:
            file.write(date + '\n')


# 4. Чтение дат из файла
def read_dates_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        dates = [line.strip() for line in file.readlines()]
    return dates


# Основной блок выполнения
if __name__ == "__main__":
    # Шаг 1: Найти даты в исходном файле
    dates = read_and_find_dates('texts.txt')
    print("Найденные даты:", dates)

    # Шаг 2: Преобразовать даты в нужный формат
    converted_dates = convert_date_format(dates)
    print("Преобразованные даты:", converted_dates)

    # Шаг 3: Сохранить преобразованные даты в файл
    save_dates_to_file(converted_dates, 'dates.txt')
    print("Даты сохранены в файл dates.txt")

    # Шаг 4: Прочитать даты из файла и отсортировать их
    dates_from_file = read_dates_from_file('dates.txt')
    sorted_dates = sorted(dates_from_file, key=lambda date: date)

    # Вывод отсортированных дат
    print("Отсортированные даты:")
    for date in sorted_dates:
        print(date)