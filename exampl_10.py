# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

N=int(input('Введите количество монеток: '))
reshka = 0
orel = 0
i = 0

while i<N:
    X=int(input(f'Если монетка {i+1} перевернута решкой, то введите 1, иначе 0: '))
    i+= 1
    if X==0:
        reshka+= 1
    else: orel+= 1


if reshka > orel:
    print (f'Нужно перевернуть монет: {N-reshka}')
else: print (f'Нужно перевернуть монет: {N-orel}')