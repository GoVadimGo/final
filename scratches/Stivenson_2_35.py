# Напишите программу, запрашивающую у пользователя целое число и выводящую
# на экран информацию о том, являетс введенное число четным или нечетным.

NUM = int(input('Enter number: '))

if NUM % 2 == 0 :
    print('Even number')
else:
    print('Odd number')