# Задача 2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

n = int(input('Введите число N: '))
m = n # сохраняем для вывода
lst = [] # создаем пустой список для множителей
multip = 2 # множитель для деления
while n > 1:
    if n % multip == 0: # пока делится без остатка на множитель..
        lst.append(multip) # .. добавляем множитель в список
        n = int(n / multip) # делим на множитель
    else:
        multip += 1 # если не делится на множитель, то увеличиваем множитель на 1
print(f'{m} = ', end='')
print(*lst, sep='*')