name = 0
lname = 0
yearbthd = 0
city = 0
emale = 0
tel = 0
def funk(name, lname, yearbthd, city, emale, tel):
    data = []
    name = input('Введите Ваше имя - ')
    lname = input('Введите Вашу фамилию - ')
    yearbthd = input('Введите Год Вашего рождения - ')
    city = input('Введите город Вашего проживания - ')
    emale = input('Введите Ваш электронный адрес - ')
    tel = input('Введите Ваш телефон - ')
    print('Мы получили следующие данные: ')
    data.append(name)
    data.append(lname)
    data.append(yearbthd)
    data.append(city)
    data.append(emale)
    data.append(tel)
    return data

print(funk(name, lname, yearbthd, city, emale, tel))
