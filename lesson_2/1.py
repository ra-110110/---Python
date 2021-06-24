# Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
# info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие
# и считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения
# параметров «Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить
# в соответствующий список. Должно получиться четыре списка —
# например, os_prod_list, os_name_list, os_code_list, os_type_list.
# В этой же функции создать главный список для
# хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка:
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде
# списка и поместить в файл main_data (также для каждого файла);


# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
# В этой функции реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных данных
# в соответствующий CSV-файл;


# Проверить работу программы через вызов функции write_to_csv().
import csv


def get_data():
    files_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    result = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for file_name in files_list:
        # print(file_name)
        with open(file_name, encoding='windows-1251') as data_file:
            data = data_file.read().split('\n')
            for i in data:
                row_data = i.split(':')
                if 'Изготовитель системы' in row_data[0]:
                    os_prod_list.append(row_data[1].strip(''))
                if 'Название ОС' in row_data[0]:
                    os_name_list.append(row_data[1].strip(''))
                if 'Код продукта' in row_data[0]:
                    os_code_list.append(row_data[1].strip(''))
                if 'Тип системы' in row_data[0]:
                    os_type_list.append(row_data[1].strip(''))
            result.append(
                [
                    os_prod_list[-1],
                    os_name_list[:1][0],
                    os_code_list[:1][0],
                    os_type_list[:1][0]
                ]
            )
    return result


def write_to_csv(file_name):
    with open(file_name, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        print(get_data())
        for row in get_data():
            csv_writer.writerow(row)


write_to_csv('new_test.csv')
