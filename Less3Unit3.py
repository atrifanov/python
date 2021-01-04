a = 0
b = 0
c = 0
def my_funk(a, b, c):
    data = []
    a = int(input('Введите первое число - '))
    b = int(input('Введите второе число - '))
    c = int(input('Введите третье число - '))
    data.append(a)
    data.append(b)
    data.append(c)
    print('Вы ввели следующие числа: ')
    print(data)
    i = 0
    if data[i] < data[i + 1] and data[i] < data[i + 2]:
        data.pop(i)
    elif data[i + 1] < data[i + 2]:
        data.pop(i + 1)
    else: data.pop(i + 2)
    result = sum(data)
    print('Сумма двух самых больших чисел равна: ')
    return result

print(my_funk(a, b, c))
