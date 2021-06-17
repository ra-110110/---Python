# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.

my_file = open("New_File.txt", "w+")
my_file.write('сетевое программирование' + '\n' + 'сокет' + '\n' + 'декоратор' + '\n')
my_file.close()

import locale

def_coding = locale.getpreferredencoding()
print(def_coding)

with open('New_File.txt') as f_n:
    for line in f_n:
        line = line.encode('utf-8').decode('utf-8')
        print(line, end='')
