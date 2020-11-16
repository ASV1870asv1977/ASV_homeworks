"""
Задача № 2.  Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('task_2.txt', 'r', encoding='utf-8') as f:
    print(f'{"-" * 50}\nФайл {f.name}:\n{f.read()}\n')
    f.seek(0)
    my_list = f.readlines()

print(f'Содержит {len(my_list)} строки.')
for i in range(len(my_list)):
    print(f'{i + 1}-я строка содержит {len(my_list[i].split())} слов')








