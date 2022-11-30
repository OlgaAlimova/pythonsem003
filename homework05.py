# Задайте число. Составьте список чисел Фибоначчи, в том числе
# для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите число: '))
my_list = []
m1 = 0
my_list.append(m1)
m2 = 1
my_list.append(m2)
n1 = 1
n2 = m1
for i in range(2, k+1):
    m3 = m2 + m1
    n3 = n1-n2
    my_list.append(m3)
    my_list.insert(0, n3)
    m1 = m2
    m2 = m3
    n1 = n2
    n2 = n3
my_list.insert(0, (n1-n2))
print(my_list)
