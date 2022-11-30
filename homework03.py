# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

count = int(input('Введите количество элементов списка: '))
my_list = []
for i in range(count):
    my_list.append(random.uniform(1, 10))
print(my_list)

indrob_list = []
for j in range(len(my_list)):
    temp = my_list[j] % 1
    indrob_list.append(temp)
print(indrob_list)

max_el = indrob_list[0]
for current_el in indrob_list:
    if current_el > max_el:
        max_el = current_el
print(max_el)

min_el = indrob_list[0]
for current_el in indrob_list:
    if current_el < min_el:
        min_el = current_el
print(min_el)

difference_numbers = max_el - min_el
print(f'Разница между максимальным и минимальным значением дробной части = {round(difference_numbers, 2)}')