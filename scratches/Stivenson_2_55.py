# Запросите у  пользователя длину волны и  выведите на экран соответствующий ей цвет.
# Если введенное пользователем значение длины волны окажется за пределами видимой части
# спектра, сообщите об этом.

LENGTH = int(input('Введите длину волны : '))

if LENGTH >= 380 and LENGTH <450:
    print('Viola')
elif LENGTH >= 450 and LENGTH < 495:
    print('Blue')
elif LENGTH >=495 and LENGTH < 570:
    print('Green')
elif LENGTH >= 570 and LENGTH < 590:
    print('Yellow')
elif LENGTH >= 590 and LENGTH < 620:
    print('Orange')
elif LENGTH >= 630 and LENGTH <= 750:
    print('Red')
else:
    print('Wrong length')