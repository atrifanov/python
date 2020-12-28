# Строка

a = input('Введите строку из нескольких слов, разделённых пробелами: ')

b = a.split()
for index, elem in enumerate(b):
    print(index, elem[0:10])