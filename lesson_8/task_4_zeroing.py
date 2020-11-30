# ----------------------------------------------------------------------------------------------------------------------
# Program by Sergey A.
# LogisticsStoreHouse
#
# Version           Data               Info
#  1.1             2020/30        Initial Version
# ______________________________________________________________________________________________________________________
"""
!!!!!!!!!!
Запуск модуля инициирует ОБНУЛЕНИЕ информации из базы данных склада
!!!!!!!!!!
"""
import pickle, storehouse

test_comp_obj = storehouse.Computer('1', '1', '1')
test_monit_obj = storehouse.Monitor('1', '1', '1')
test_print_obj = storehouse.Printer('1', '1', '1')
equipment_sum = 0
computer_sum = 0
monitor_sum = 0
printer_sum = 0
sum_obj = 0

super_db = [equipment_sum, {'компьютер': [computer_sum, [sum_obj, test_comp_obj]],
                            'монитор': [monitor_sum, [sum_obj, test_monit_obj]],
                            'принтер': [printer_sum, [sum_obj, test_print_obj]]}]

with open('super_db.pic', 'wb') as f:
    pickle.dump(super_db, f)

with open('super_db.pic', 'rb') as f:
    super_db = pickle.load(f)
    print(super_db)

print(super_db[1]['компьютер'][1][1].__dict__)

