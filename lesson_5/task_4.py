"""
Задача № 3.  Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
"""

rus_numbers = {0: 'Ноль',
               1: 'Один',
               2: 'Два',
               3: 'Три',
               4: 'Четыре',
               5: 'Пять',
               6: 'Шесть',
               7: 'Семь',
               8: 'Восемь',
               9: 'Девять'}

# Чтение файла построчно с предворительным выводом содержимого
with open('task_4_eng.txt', 'r', encoding='utf-8') as f:
    print(f'{"-" * 50}\nФайл {f.name}:\n{f.read()}\n')
    f.seek(0)
    my_list = f.readlines()

# Замена английских числительных на русские
my_list_rus = []
for i in range(len(my_list)):
    number_list = my_list[i].replace('\n', '').split()
    for key in rus_numbers:
        if key == int(number_list[2]):
            number_list[0] = rus_numbers[key]
    my_list_rus.append(f'{" ".join(number_list)}\n')

# Запись измененного списка построчно в новый файл
with open('task_4_rus.txt', 'w', encoding='utf-8') as f:
    f.writelines(my_list_rus)

# Чтение и вывод содержимого нового файла
with open('task_4_rus.txt', 'r', encoding='utf-8') as f:
    print(f'{"-" * 50}\nФайл {f.name}:\n{f.read()}\n')
