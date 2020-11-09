"""
Задача № 6.  Реализовать функцию int_func(), принимающую слово
из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
"""

def capital_letter(text):
    """
    Функция принимает строку, формирует из нее список, заменяет первую букву элемента списка
    на заглавную и возвращает строку элементов списка.

    :param text (str): аргумент
    :return (str): строка, где каждое слово с заглавной буквы
    """
    text = text.split()
    for i in range(len(text)):
        text[i] = text[i].title()
    text = ' '.join(text)
    return text

while True:
    my_word = input('Для выхода введите "q"\nВведите слово или фразу из маленьких латинских букв через пробел: ')
    print('-' * 50)
    if my_word == 'q':
        print('Выход')
        break
    for word in my_word:
        n = 0
        if  75 < ord(word) < 123 or ord(word) == 32:
            pass
        else:
            print(f'Введенное значение не соответствует условиям\n{"=" * 50}')
            n = 1
            break
    if n == 1: continue

    print(f'Исправленный текст:\n{capital_letter(my_word)}\n{"=" * 50}')
