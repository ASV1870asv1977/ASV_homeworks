"""
Задача № 1
Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные,
выведите на экран.
"""
a_int = int(input('Введите целое число (Пример: 10): '))
b_float = float(input('Введите число с плавающей точкой (Пример: 10.2): '))
c_str = input('Введите текст (Пример: abc): ')
d_bool = bool(input('Введите логическое значение (Пример: True): '))

my_list = [a_int, b_float, c_str, d_bool]
my_dict = {'int': 10, 'float': 10.2, 'str': 'abc', 'bool': True}
my_tuple = (a_int, b_float, c_str, d_bool)
my_set = {a_int, b_float, c_str, d_bool}
super_list = [my_list, my_dict, my_tuple, my_set]

print(('-' * 50))

for i in my_list:
    print(f'Переменная со значением {i} имеет тип {type(i)}')

for i in super_list:
    print(f'Переменная со значением {i} имеет тип {type(i)}')




