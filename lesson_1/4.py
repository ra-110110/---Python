# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
# и выполнить обратное преобразование (используя методы encode и decode).

word_1 = 'разработка'
word_2 = 'администрирование'
word_3 = 'protocol'
word_4 = 'standard'

bytes_word_1 = word_1.encode('utf-8')
bytes_word_2 = word_2.encode('utf-8')
bytes_word_3 = word_3.encode('utf-8')
bytes_word_4 = word_4.encode('utf-8')

print(bytes_word_1)
print(bytes_word_2)
print(bytes_word_3)
print(bytes_word_4)

print(bytes_word_1.decode('utf-8'))
print(bytes_word_2.decode('utf-8'))
print(bytes_word_3.decode('utf-8'))
print(bytes_word_4.decode('utf-8'))
