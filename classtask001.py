# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

my_list = ['654564dkfhghg', '879885kdjfhgkjb', '2124543xnbvvbdv']

n = input('Введите число, которое необходимо найти: ')
trigger = True
for item in my_list:
    for j in item:
        if j == n:
            print(f'Да, число {n} присутствует в элементе {item}')
            trigger = False
            break
        # else:
if trigger == 1:
    print('Такого числа в списке нет')
