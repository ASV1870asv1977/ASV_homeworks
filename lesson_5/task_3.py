"""
Задача № 3.  Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""

with open('task_3.txt', 'r', encoding='utf-8') as f:
    print(f'{"-" * 50}\nФайл {f.name}\n"Список окладов сотрудников":\n{f.read()}\n')
    f.seek(0)
    my_list = f.readlines()

jonahs = []
income = 0
for i in range(len(my_list)):
    emploe_list = my_list[i].replace('\n', '').split()
    income += float(emploe_list[1])
    if float(emploe_list[1]) < 20000:
        jonahs.append(emploe_list[0])

print(f'Сотрудники с окладом менее 20000:')
[print(i) for i in jonahs]
print(f'Средняя величина дохода всех сотрудников: {income / len(my_list)}')


