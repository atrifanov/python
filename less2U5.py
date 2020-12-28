# Рейтинг

list = [7, 7, 5, 3, 3, 2]

print('У нас есть рейтинг:', list)

user = int(input('Введите новый элемент рейтинга: '))

if user in list:
        new_index = list.index(user) + list.count(user) - 1
        list.insert(new_index, user)
elif user > max(list):
        list.insert(0, user)
elif user <= min(list):
        list.insert(len(list), user)
else:
    for i in range(0, len(list)-1):
        if list[i+1] < user < list[i]:
                list.insert(i+1, user)

print('Новый рейтинг:')
print(', '.join(map(str, list)))