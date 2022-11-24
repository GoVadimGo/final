# В данном упражнении вы создадите программу для отображения стандартной таблицы умножения от единицы до десяти.
# При этом ваша таблица умножения должна иметь заголовки над первой строкой и слева от первого столбца,
# как показано в представленном примере.

# пределы циклов (и таблицы)
MIN = 1
MAX = 10

# выводим шкалу таблицы

print('    ',end='') # делаем отступ ,так же end='' не переносит цикл на новую строку, а продолжает после отступа
for x in range(MIN,MAX+1):
    print('%4d' %x , end='') # выводим шкалу с интервалом "4" между друг другом
# что бы следующий код выходил на новую строку, заканчиваем цикл новой строкой.
print()
# выводим саму таблицу внешним и внутренним циклом

for x in range(MIN,MAX+1):
    print('%4d' %x, end='') # делаем интервал между цифрами "4" , так же каждый цикл будет иметь продолжение внутренним
    # циклом с помощью end=''
    for y in range(MIN,MAX+1):
        print('%4d' %(x*y),end='') # внутренний цикл будет выводить строку из цифр каждый раз за внешним циклом
        # код внутреннего цикла : переменная внешнего цикла перемножается с каждой переменной внутреннего.
        # каждый раз ,когда внутренний цикл заканчивается, выводится команда новой строки"!
    print()


