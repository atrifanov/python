#  проверка числа

list = [6, 9876, 'lkjhgfd',  ['r', 65656], '8765433333322', 'kjhg kjhg jhgf', 'lkh', True, False]

print('Cписок:\n{}'.format(list))

for i in range(len(list)):
    print('Элемент списка "{}" относится к {}.'.format(list[i], type(list[i])))