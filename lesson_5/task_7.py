"""
Задача № 7.  Создать (не программно) текстовый файл, в котором каждая строка должна содержать
данные о фирме: название, форма собственности, выручка, издержки.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Итоговый список сохранить в виде json-объекта в соответствующий файл.
"""

import json

# Чтение из файла, создание исходного списка
with open('task_7.txt', 'r', encoding='utf-8') as f:
    print(f'{"-" * 50}\nФайл {f.name}:\n{f.read()}')
    f.seek(0)
    company_list = f.readlines()

print("-" * 50)
company_dict = {}
aver_profit = 0
n = 0

for val in company_list:
    firm = val.split()                                    # Создание списка каждой компании
    for a in range(2, len(firm)):
        firm[a] = int(firm[a])
    profit = firm[2] - firm[3]
    print(f'Прибыль компании {firm[0]}: {profit}')
    if profit > 0:
        aver_profit += profit
        n += 1
    company_dict[firm[0].replace('"', '')] = profit       # Добавление в словарь требуемых данных

aver_profit = aver_profit / n
aver_profit_dict = dict(average_profit=round(aver_profit, 2)) # Создание словаря со средним доходом
new_comp_list = [company_dict, aver_profit_dict]          # Формирование списка установленного образца

print(f'{"-" * 50}\nСредняя прибыль доходных компаний: {round(aver_profit, 2)}')
print(f'Список установленной формы:\n{new_comp_list}')

with open('company.json', 'w', encoding='utf-8') as f:
    json.dump(new_comp_list, f)
    print(f'Список доходности компаний сохранен в файле: {f.name}')
