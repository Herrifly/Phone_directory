from typing import Dict
import pandas as pd

INFO_TEMPLATE: Dict = {
    'Фамилия': '',
    'Имя': "",
    "Отчество": "",
    "Организация": "",
    "Рабочий тел.": "",
    "Сотовый тел.": ""
}

# убираем ограничения вывода, чтобы в консоли все поля были видны
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 6)


def print_all(file_name: str):
    """Функция выводит всю информацию о номерах в виде таблицы"""

    df = pd.read_table(file_name, sep=';')
    print(df)


def add_phone(file_name: str, info_template: Dict):
    """Функция получает данные, введенные через консоль, и добавляет их все одной строкой в наш файл"""

    df = pd.read_table(file_name, sep=';')

    print('Введите информацию о новом номере')
    for key in info_template:
        info_template[key] = input(f'{key}: ')
    df.loc[len(df.index)] = list(info_template.values())
    df.to_csv(file_name, index=False, sep=';')
    print("\nИнформация успешно добавлена!")


def search_info(file_name: str, info_template: Dict):
    """Функция получает все имеющиеся у нас данные и выводит все подошедшие под условия контакты"""

    print('Введите информацию о номере, по которой ищем, если поле неизвестно нажмите Enter')

    df = pd.read_table(file_name, sep=';')
    size: int = df.size
    for key in info_template:
        info_template[key] = input(f'{key}: ')
        if info_template[key] != '':
            df = df.loc[df[key] == info_template[key]]
    if size == df.size or df.size == 0:
        raise "Контакта с такими данными не найдено!"

    print("\nВот найденные телефоны:\n")

    print(df)


def update(file_name: str, info_template: Dict, idx: int):
    """Функция получает на вход помимо названия файла и шаблона еще и индекс контакта,
    индекс можно найти через функцию search_info (число рядом со строкой нужного контакта)"""

    df = pd.read_table(file_name, sep=';')
    print("Введите данные обновленные данные ниже, если поле не меняем нажмите Enter")
    for key in info_template:
        info_template[key] = input(f'{key}: ')
        if info_template[key] != '':
            df.at[idx, key] = info_template[key]

    df.to_csv(file_name, index=False, sep=';')
    print("Данные обновлены!")
