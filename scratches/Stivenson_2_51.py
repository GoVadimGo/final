# Напишите программу, вычисляющую действительные корни квадратичной
# функции. Сначала вы должны запросить у пользователя значения  a , b и c.
# После этого должно быть выведено на экран количество действительных корней функции и их значения.

A,B,C = input('Введите 3 числа : ').split() # Введенные числа раскидываем по переменным.
A,B,C = [int(A),int(B),int(C)] # из стринг делаем инт числа

D = B**2 - 4*A*C

if D == 0 :
    x= -(B/2*A)
    print(f'У квадратного уравнения один действительный корень : x - {x}.')
elif D >0 :
    x_1 = (-B + D**0.5)/2*A
    x_2 = (-B - D**0.5)/2*A
    print(f'У квадратного уравнения два действительных корня : x1 - {x_1} , x2 - {x_2}.')
else:
    print('Действительных корней нет.')

