# Напишите программу, которая будет запрашивать у пользователя значение
# частоты волны и отображать название соответствующего излучения.

A,B,C = input('Введите диапазон частоты : ').split()
A,B,C = int(A),int(B),int(C)
ABC = A * B**C

if ABC < 3*10**9:
    print('Радиоволны')
elif ABC > 3*10**9 and ABC <3*10**12:
    print('Микороволны')
elif ABC > 3*10*12 and ABC < 4.3*10**14:
    print('Инфракрасное излучение')
elif ABC > 4.3*10**14 and ABC < 7.5*10**14:
    print('Видимое излучение')
elif ABC > 7.5*10**14 and ABC < 3*10**17:
    print('Ультрафиалетовое излучение')
elif ABC > 3*10*17 and ABC < 3*10**19:
    print('Рентгеновоское излучение')
else:
    print('Гамма излучение')