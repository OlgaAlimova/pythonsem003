# Напишите программу, которая будет преобразовывать десятичное число
# в двоичное. Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

decimal_number = int(input('Введите десятичное число: '))
my_list = []
while decimal_number > 0:
    temp = decimal_number % 2
    # print(f'temp = {temp}')
    decimal_number = decimal_number // 2
    # print(f'decimal_number = {decimal_number}')
    my_list.append(temp)
# print(my_list)
new_list = my_list[::-1]
print(*new_list, sep='')
