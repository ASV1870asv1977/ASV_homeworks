# ----------------------------------------------------------------------------------------------------------------------
# Program by Sergey A.
# LogisticsStoreHouse
#
# modules: task_4_sh_index_v1.py (main)
#          storehouse.py (classes and functions)
#          task_4_zeroing.py (reset settings)
#          super_db.pic (database storage)
#          journal.txt (storage of log data)
#          counter.txt (counter data storage)
#
# Version           Data               Info
#  1.1             2020/30        Initial Version
# ______________________________________________________________________________________________________________________


import storehouse, datetime, pickle
from tkinter import *
from tkinter import ttk, messagebox, scrolledtext, Radiobutton
from tkinter.ttk import Combobox


# Кнопка выбора типа оборудования
def clicked_1():
    if combo2.get() == 'компьютер':
        text1 = '           Процессор:'
        text2 = 'Операционная система:'
    elif combo2.get() == 'монитор':
        text1 = '              Модель:'
        text2 = '                       Диагональ:'
    elif combo2.get() == 'принтер':
        text1 = '              Модель:'
        text2 = '                       Цветность:'
    else:
        text1 = ''
        text2 = ''

    Label(tab1, text=f'{text1}', justify=LEFT, font=("Arial Bold", 12)).grid(column=0, row=11, sticky=E)
    Label(tab1, text=f'{text2}', justify=LEFT, font=("Arial Bold", 12)).grid(column=0, row=12, sticky=E)


# "Проверка" правильности заполнения полей
def clicked_2():
    txt1 = Entry(tab1, textvariable=txt1_message, state='disabled', width=23).grid(column=1, row=5, sticky=W)
    txt2 = Entry(tab1, textvariable=txt2_message, state='disabled', width=23).grid(column=1, row=6, sticky=W)
    txt5 = Entry(tab1, textvariable=txt5_message, state='disabled', width=23).grid(column=3, row=5, sticky=W)
    txt6 = Entry(tab1, textvariable=txt6_message, state='disabled', width=23).grid(column=3, row=6, sticky=W)
    txt7 = Entry(tab1, textvariable=txt7_message, state='disabled', width=23).grid(column=1, row=11, sticky=W)
    txt8 = Entry(tab1, textvariable=txt8_message, state='disabled', width=23).grid(column=1, row=12, sticky=W)
    btn1 = Button(tab1, text="применить", state='disabled', command=clicked_1).grid(column=1, row=8, sticky=W)
    combo2.config(state='disabled')
    combo1.config(state='disabled')
    rad1 = Radiobutton(tab1, text='ПОЛУЧЕНИЕ', state='disabled', command=radio_1, value=1,
                       font=("Arial Bold", 12)).grid(column=1, row=2)
    rad2 = Radiobutton(tab1, text='ВЫДАЧА', state='disabled', command=radio_2, value=2, font=("Arial Bold", 12)).grid(
        column=2, row=2)
    btn2 = Button(tab1, text="ПРОВЕРКА", state='disabled', command=clicked_2, background="#3CB371",
                  foreground="#000").place(x=200, y=300)
    btn3 = Button(tab1, text=" ОТМЕНА ", state='normal', command=clicked_3, background="#FFD700",
                  foreground="#000").place(x=350, y=300)

    if not txt1_message.get() or not txt2_message.get() or not txt5_message.get() or not txt6_message.get() \
            or not txt7_message.get() or not txt8_message.get() or combo1.get() == '' or combo2.get() == '':
        messagebox.showinfo('Внимание', 'Не введены данные обязательные к заполнению')
        btn4 = Button(tab1, text="ПРОВЕСТИ", state='disabled', command=clicked_4, background="#FF6347",
                      foreground="#000").place(x=500, y=300)
    elif not txt2_message.get().isdigit():
        messagebox.showinfo('Внимание', 'Не введено цифровое значение количества оборудования')
        btn4 = Button(tab1, text="ПРОВЕСТИ", state='disabled', command=clicked_4, background="#FF6347",
                      foreground="#000").place(x=500, y=300)
    elif not txt6_message.get().isdigit():
        messagebox.showinfo('Внимание', 'Не введено цифровое значение года изготовления оборудования')
        btn4 = Button(tab1, text="ПРОВЕСТИ", state='disabled', command=clicked_4, background="#FF6347",
                      foreground="#000").place(x=500, y=300)
    elif not storehouse.Storehouse.numbers_valid(txt6_message.get(), date_now.year):
        messagebox.showinfo('Внимание', 'Указан некорректный год изготовления оборудования')
        btn4 = Button(tab1, text="ПРОВЕСТИ", state='disabled', command=clicked_4, background="#FF6347",
                      foreground="#000").place(x=500, y=300)

    elif not storehouse.Storehouse.quantity_valid(txt2_message.get()):
        messagebox.showinfo('Внимание', 'Введено значение количества техники менее одного')
        btn4 = Button(tab1, text="ПРОВЕСТИ", state='disabled', command=clicked_4, background="#FF6347",
                      foreground="#000").place(x=500, y=300)
    else:
        btn4 = Button(tab1, text="ПРОВЕСТИ", state='normal', command=clicked_4, background="#FF6347",
                      foreground="#000").place(x=500, y=300)


# Кнопка "Отмена"
def clicked_3():
    txt1 = Entry(tab1, state='normal', textvariable=txt1_message, width=23).grid(column=1, row=5, sticky=W)
    txt2 = Entry(tab1, state='normal', textvariable=txt2_message, width=23).grid(column=1, row=6, sticky=W)
    txt5 = Entry(tab1, state='normal', textvariable=txt5_message, width=23).grid(column=3, row=5, sticky=W)
    txt6 = Entry(tab1, state='normal', textvariable=txt6_message, width=23).grid(column=3, row=6, sticky=W)
    txt7 = Entry(tab1, state='normal', textvariable=txt7_message, width=23).grid(column=1, row=11, sticky=W)
    txt8 = Entry(tab1, state='normal', textvariable=txt8_message, width=23).grid(column=1, row=12, sticky=W)
    btn1 = Button(tab1, state='normal', text="применить", command=clicked_1).grid(column=1, row=8, sticky=W)
    combo2.config(state='normal')
    combo1.config(state='normal')
    rad1 = Radiobutton(tab1, state='normal', text='ПОЛУЧЕНИЕ', command=radio_1, value=1, font=("Arial Bold", 12)).grid(
        column=1, row=2)
    rad2 = Radiobutton(tab1, state='normal', text='ВЫДАЧА', command=radio_2, value=2, font=("Arial Bold", 12)).grid(
        column=2, row=2)
    btn2 = Button(tab1, text="ПРОВЕРКА", state='normal', command=clicked_2, background="#3CB371",
                  foreground="#000").place(x=200, y=300)
    btn3 = Button(tab1, text=" ОТМЕНА ", state='disabled', command=clicked_3, background="#FFD700",
                  foreground="#000").place(x=350, y=300)
    btn4 = Button(tab1, text="ПРОВЕСТИ", state='disabled', command=clicked_3, background="#FF6347",
                  foreground="#000").place(x=500, y=300)


# Кнопка "Провести" записывает (удаляет) информацию из базы данных
def clicked_4():
    global counter_1, text_act
    counter_1 += 1
    if text_act == 'Получение на склад от':
        counter_radio = 1
    if text_act == 'Выдача со склада в':
        counter_radio = 0

    btn4 = Button(tab1, text="ПРОВЕСТИ", state='disabled', command=clicked_3, background="#FF6347",
                  foreground="#000").place(x=500, y=300)
    with open('super_db.pic', 'rb') as f:
        super_db = pickle.load(f)

    # Журнал учета движения материальных средств
    a = [str(counter_1), str(date_store), str(text_act), str(txt1_message.get()), str(combo2.get()),
         str(txt5_message.get()), str(txt8_message.get()),
         str(txt7_message.get()), str(txt6_message.get()), str(txt2_message.get()), str(combo1.get())]
    a_str1 = ' '.join(a)
    txt.insert(INSERT, f'{a_str1}\n')

    with open('counter.txt', 'w') as f:
        f.write(str(counter_1))
    quant_temp = storehouse.Storehouse.arrival(int(txt2_message.get()), counter_radio)

    if combo2.get() == 'компьютер':
        user_object_temp = storehouse.Computer(txt7_message.get().lower(), txt8_message.get().lower(),
                                               txt5_message.get().lower(), int(txt6_message.get()))
        if counter_radio == 1:
            super_db[0] += quant_temp
            super_db[1]['компьютер'][0] += quant_temp
            for i in range(1, len(super_db[1]['компьютер'])):
                if super_db[1]['компьютер'][i][1].__dict__ == user_object_temp.__dict__:
                    super_db[1]['компьютер'][i][0] += quant_temp
                    messagebox.showinfo('Внимание', 'Увеличено количество оборудования имеющейся конфигурации')
                    break
            else:
                super_db[1]['компьютер'].append([quant_temp, user_object_temp])
                messagebox.showinfo('Внимание', 'Добавлена новая конфигурация оборудования')
            a_str = '   Проведено'

        if counter_radio == 0:
            for i in range(1, len(super_db[1]['компьютер'])):
                if super_db[1]['компьютер'][i][1].__dict__ == user_object_temp.__dict__ \
                        and super_db[1]['компьютер'][i][0] >= abs(quant_temp):
                    super_db[1]['компьютер'][i][0] += quant_temp
                    messagebox.showinfo('Внимание', 'Указанная конфигурация списана со склада')
                    super_db[0] += quant_temp
                    super_db[1]['компьютер'][0] += quant_temp
                    a_str = '   Проведено'
                    break
            else:
                a_str = '   Не проведено'
                messagebox.showinfo('Внимание', 'Списание не проведено!\nОтсутствие:\n'
                                                '- указанной конфигурации;\n'
                                                '- количества оборудования указанной конфигурации.\n'
                                                'Смотри наличие на складе.')

    elif combo2.get() == 'монитор':
        user_object_temp = storehouse.Monitor(txt7_message.get().lower(), txt8_message.get().lower(),
                                              txt5_message.get().lower(), int(txt6_message.get()))
        if counter_radio == 1:
            super_db[0] += quant_temp
            super_db[1]['монитор'][0] += quant_temp
            for i in range(1, len(super_db[1]['монитор'])):
                if super_db[1]['монитор'][i][1].__dict__ == user_object_temp.__dict__:
                    super_db[1]['монитор'][i][0] += quant_temp
                    messagebox.showinfo('Внимание', 'Увеличено количество оборудования имеющейся конфигурации')
                    break
            else:
                super_db[1]['монитор'].append([quant_temp, user_object_temp])
                messagebox.showinfo('Внимание', 'Добавлена новая конфигурация оборудования')
            a_str = '   Проведено'

        if counter_radio == 0:
            for i in range(1, len(super_db[1]['монитор'])):
                if super_db[1]['монитор'][i][1].__dict__ == user_object_temp.__dict__ \
                        and super_db[1]['компьютер'][i][0] >= abs(quant_temp):
                    super_db[1]['монитор'][i][0] += quant_temp
                    messagebox.showinfo('Внимание', 'Указанная конфигурация списана со склада')
                    super_db[0] += quant_temp
                    super_db[1]['монитор'][0] += quant_temp
                    a_str = '   Проведено'
                    break
            else:
                a_str = '   Не проведено'
                messagebox.showinfo('Внимание', 'Списание не проведено!\nОтсутствие:\n'
                                                '- указанной конфигурации;\n'
                                                '- количества оборудования указанной конфигурации.\n'
                                                'Смотри наличие на складе.')

    elif combo2.get() == 'принтер':
        user_object_temp = storehouse.Printer(txt7_message.get().lower(), txt8_message.get().lower(),
                                              txt5_message.get().lower(), int(txt6_message.get()))
        if counter_radio == 1:
            super_db[0] += quant_temp
            super_db[1]['принтер'][0] += quant_temp
            for i in range(1, len(super_db[1]['принтер'])):
                if super_db[1]['принтер'][i][1].__dict__ == user_object_temp.__dict__:
                    super_db[1]['принтер'][i][0] += quant_temp
                    messagebox.showinfo('Внимание', 'Увеличено количество оборудования имеющейся конфигурации')
                    break
            else:
                super_db[1]['принтер'].append([quant_temp, user_object_temp])
                messagebox.showinfo('Внимание', 'Добавлена новая конфигурация оборудования')
            a_str = '   Проведено'

        if counter_radio == 0:
            for i in range(1, len(super_db[1]['принтер'])):
                if super_db[1]['принтер'][i][1].__dict__ == user_object_temp.__dict__ \
                        and super_db[1]['компьютер'][i][0] >= abs(quant_temp):
                    super_db[1]['принтер'][i][0] += quant_temp
                    messagebox.showinfo('Внимание', 'Указанная конфигурация списана со склада')
                    super_db[0] += quant_temp
                    super_db[1]['принтер'][0] += quant_temp
                    a_str = '   Проведено'
                    break
            else:
                a_str = '   Не проведено'
                messagebox.showinfo('Внимание', 'Списание не проведено!\nОтсутствие:\n'
                                                '- указанной конфигурации;\n'
                                                '- количества оборудования указанной конфигурации.\n'
                                                'Смотри наличие на складе.')
    txt.insert(INSERT, f'{a_str}\n')

    with open('journal.txt', 'a', encoding='utf-8') as f:
        f.write(f'{a_str1}\n{a_str}\n')

    with open('super_db.pic', 'wb') as f:
        pickle.dump(super_db, f)
    print(super_db)


def radio_1():
    global text_act
    lbl1 = Label(tab1, text=f'Грузоотправитель', justify=LEFT, font=("Arial Bold", 12)).grid(column=0, row=5, sticky=E)
    text_act = 'Получение на склад от'


def radio_2():
    global text_act
    lbl1 = Label(tab1, text=f'  Грузополучатель', justify=LEFT, font=("Arial Bold", 12)).grid(column=0, row=5, sticky=E)
    text_act = 'Выдача со склада в'


def clicked_ful():
    with open('super_db.pic', 'rb') as f:
        super_db = pickle.load(f)
    txt_report.delete(1.0, END)

    if super_db[0] == 0:
        txt_report.insert(INSERT, 'На складе оборудование отсутствует')
        return
    txt_report.insert(INSERT, f'Всего оборудования на складе: {super_db[0]} ед.\n')

    for equipment in super_db[1]:
        txt_report.insert(INSERT, f'\nОборудование {equipment}ы {super_db[1][equipment][0]} ед.:\n')
        if not super_db[1][equipment][0]:
            txt_report.insert(INSERT, f'отсутствует\n')

        for i in range(2, len(super_db[1][equipment])):
            if equipment == 'компьютер':
                txt_report.insert(INSERT, f'{super_db[1][equipment][i][1].manufacturer.upper()}, '
                                          f'прцессор: {super_db[1][equipment][i][1].cpu}, '
                                          f'операционная система: {super_db[1][equipment][i][1].os.upper()}, '
                                          f'год выпуска: {super_db[1][equipment][i][1].year}, '
                                          f'на складе {super_db[1][equipment][i][0]} ед.\n')

            elif equipment == 'монитор':
                txt_report.insert(INSERT, f'{super_db[1][equipment][i][1].manufacturer.upper()}, '
                                          f'модель: {super_db[1][equipment][i][1].model.upper()}, '
                                          f'диагональ экрана: {super_db[1][equipment][i][1].diagonal} дюйма, '
                                          f'год выпуска: {super_db[1][equipment][i][1].year}, '
                                          f'на складе {super_db[1][equipment][i][0]} ед.\n')

            elif equipment == 'принтер':
                txt_report.insert(INSERT, f'{super_db[1][equipment][i][1].manufacturer.upper()}, '
                                          f'модель: {super_db[1][equipment][i][1].model.upper()}, '
                                          f'цветность: {super_db[1][equipment][i][1].color}, '
                                          f'год выпуска: {super_db[1][equipment][i][1].year}, '
                                          f'на складе {super_db[1][equipment][i][0]} ед.\n')


def radio_comp():
    with open('super_db.pic', 'rb') as f:
        super_db = pickle.load(f)
    txt_report.delete(1.0, END)
    equipment = 'компьютер'
    txt_report.insert(INSERT, f'Оборудование {equipment}ы {super_db[1][equipment][0]} ед.:\n\n')
    if not super_db[1][equipment][0]:
        txt_report.insert(INSERT, f'отсутствует\n')
    for i in range(2, len(super_db[1][equipment])):
        txt_report.insert(INSERT, f'{super_db[1][equipment][i][1].manufacturer.upper()}, '
                                  f'прцессор: {super_db[1][equipment][i][1].cpu}, '
                                  f'операционная система: {super_db[1][equipment][i][1].os.upper()}, '
                                  f'год выпуска: {super_db[1][equipment][i][1].year}, '
                                  f'на складе {super_db[1][equipment][i][0]} ед.\n')


def radio_monit():
    with open('super_db.pic', 'rb') as f:
        super_db = pickle.load(f)
    txt_report.delete(1.0, END)
    equipment = 'монитор'
    txt_report.insert(INSERT, f'Оборудование {equipment}ы {super_db[1][equipment][0]} ед.:\n\n')
    if not super_db[1][equipment][0]:
        txt_report.insert(INSERT, f'отсутствует\n')
    for i in range(2, len(super_db[1][equipment])):
        txt_report.insert(INSERT, f'{super_db[1][equipment][i][1].manufacturer.upper()}, '
                                  f'модель: {super_db[1][equipment][i][1].model.upper()}, '
                                  f'диагональ экрана: {super_db[1][equipment][i][1].diagonal} дюйма, '
                                  f'год выпуска: {super_db[1][equipment][i][1].year}, '
                                  f'на складе {super_db[1][equipment][i][0]} ед.\n')


def radio_print():
    with open('super_db.pic', 'rb') as f:
        super_db = pickle.load(f)
    txt_report.delete(1.0, END)
    equipment = 'принтер'
    txt_report.insert(INSERT, f'Оборудование {equipment}ы {super_db[1][equipment][0]} ед.:\n\n')
    if not super_db[1][equipment][0]:
        txt_report.insert(INSERT, f'отсутствует\n')
    for i in range(2, len(super_db[1][equipment])):
        txt_report.insert(INSERT, f'{super_db[1][equipment][i][1].manufacturer.upper()}, '
                                  f'модель: {super_db[1][equipment][i][1].model.upper()}, '
                                  f'цветность: {super_db[1][equipment][i][1].color}, '
                                  f'год выпуска: {super_db[1][equipment][i][1].year}, '
                                  f'на складе {super_db[1][equipment][i][0]} ед.\n')


# -------------------------------------------- main ----------------------------------------------------------------

with open('counter.txt', 'r') as f:
    counter_1 = int(f.read())

text_act = None

window1 = Tk()
window1.title('Склад оргтехники')
window1.geometry('760x768')
tab_control = ttk.Notebook(window1)

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Движение материальных средств')
tab_control.pack(expand=1, fill='both')

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Создание отчета')
tab_control.pack(expand=1, fill='both')

date_now = datetime.datetime.now()
date_store = '.'.join([str(date_now.day), str(date_now.month), str(date_now.year)])

if tab1:
    lbl_col = [None, None, None, None]
    for i in range(len(lbl_col)):
        Label(tab1, text=f'{" " * 45}', font=("Arial Bold", 12)).grid(column=i, row=0)

    Label(tab1, text=f'Дата: {date_store} г.', font=("Arial Bold", 11)).place(x=520, y=250)
    Label(tab1, text=f'Кладовщик: ', justify=LEFT, font=("Arial Bold", 12)).place(x=90, y=250)

    combo1 = Combobox(tab1)
    combo1['values'] = ('Иванов И.И.', 'Петров П.П.', 'Сидоров С.С.', '')
    combo1.current(3)
    combo1.place(x=183, y=250)

    for i in range(len(lbl_col)):
        Label(tab1, text=f'{" " * 45}', font=("Arial Bold", 12)).grid(column=i, row=4)

    lbl1 = Label(tab1, text=f'Грузополучатель', justify=LEFT, font=("Arial Bold", 12)).grid(column=0, row=5, sticky=E)
    Label(tab1, text=f'Количество: ', justify=LEFT, font=("Arial Bold", 12)).grid(column=0, row=6, sticky=E)
    Label(tab1, text='Фирма-изготовитель: ', justify=LEFT, font=("Arial Bold", 12)).grid(column=2, row=5, sticky=E)
    Label(tab1, text=f'Год изготовления: ', justify=LEFT, font=("Arial Bold", 12)).grid(column=2, row=6, sticky=E)
    Label(tab1, text=f'Тип оборудования: ', justify=LEFT, font=("Arial Bold", 12)).grid(column=0, row=7, sticky=E)

    txt5_message = StringVar()
    txt5 = Entry(tab1, textvariable=txt5_message, width=23).grid(column=3, row=5, sticky=W)
    txt6_message = StringVar()
    txt6 = Entry(tab1, textvariable=txt6_message, width=23).grid(column=3, row=6, sticky=W)
    txt7_message = StringVar()
    txt7 = Entry(tab1, textvariable=txt7_message, width=23).grid(column=1, row=11, sticky=W)
    txt8_message = StringVar()
    txt8 = Entry(tab1, textvariable=txt8_message, width=23).grid(column=1, row=12, sticky=W)
    txt1_message = StringVar()
    txt1 = Entry(tab1, textvariable=txt1_message, width=23).grid(column=1, row=5, sticky=W)
    txt2_message = StringVar()
    txt2 = Entry(tab1, textvariable=txt2_message, width=23).grid(column=1, row=6, sticky=W)

    combo2 = Combobox(tab1)
    combo2['values'] = ('компьютер', 'монитор', 'принтер', '')
    combo2.current(3)
    combo2.grid(column=1, row=7, sticky=W)

    btn1 = Button(tab1, text="применить", command=clicked_1).grid(column=1, row=8, sticky=W)

    rad1 = Radiobutton(tab1, text='ПОЛУЧЕНИЕ', command=radio_1, value=1, font=("Arial Bold", 12)).grid(column=1, row=2)
    rad2 = Radiobutton(tab1, text='ВЫДАЧА', command=radio_2, value=2, font=("Arial Bold", 12)).grid(column=2, row=2)

    btn2 = Button(tab1, text="ПРОВЕРКА", command=clicked_2, background="#3CB371", foreground="#000").place(x=200, y=300)
    btn3 = Button(tab1, text=" ОТМЕНА ", state='disabled', command=clicked_3, background="#FFD700",
                  foreground="#000").place(x=350, y=300)
    btn4 = Button(tab1, text="ПРОВЕСТИ", state='disabled', command=clicked_3, background="#FF6347",
                  foreground="#000").place(x=500, y=300)

    with open('journal.txt', 'r', encoding='utf-8') as f:
        a_str = f.read()

    txt = scrolledtext.ScrolledText(tab1, width=90, height=22, font=("Arial Bold", 11))
    txt.place(x=10, y=350)
    txt.insert(INSERT, a_str)

if tab2:
    txt_report = scrolledtext.ScrolledText(tab2, width=90, height=22, font=("Arial Bold", 11))
    txt_report.place(x=10, y=350)

    Label(tab2, text=f'Полный отчет', justify=LEFT, font=("Arial Bold", 12)).place(x=15, y=15)
    btn_ful = Button(tab2, text="СОЗДАТЬ", width=12, height=1, command=clicked_ful).place(x=315, y=15)

    Label(tab2, text=f'Наличие на складе:', justify=LEFT, font=("Arial Bold", 12)).place(x=15, y=50)
    rad_comp = Radiobutton(tab2, text='Компьютеры', command=radio_comp, value=1, font=("Arial Bold", 12)).place(x=15,
                                                                                                                y=80)
    rad_monit = Radiobutton(tab2, text='Мониторы', command=radio_monit, value=2, font=("Arial Bold", 12)).place(x=165,
                                                                                                                y=80)
    rad_print = Radiobutton(tab2, text='Принтеры', command=radio_print, value=3, font=("Arial Bold", 12)).place(x=315,
                                                                                                                y=80)

window1.mainloop()
