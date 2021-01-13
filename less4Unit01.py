from sys import argv

script_name, production, rate, bonus = argv

def salary():
    return int(production) * int(rate) + int(bonus)

print(f'Зарплата сотрудника равна {salary()}')

