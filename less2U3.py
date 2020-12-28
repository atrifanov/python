# Сезоны

seas = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}

month_s = int(input('Введите номер месяца (от 1 до 12): '))

if month_s == 12 or 1 <= month_s <= 2:
    print(seas.get(1))

elif 3 <= month_s <= 5:
    print(seas.get(2))

elif 6 <= month_s <= 8:
    print(seas.get(3))

elif 9 <= month_s <= 11:
    print(seas.get(4))