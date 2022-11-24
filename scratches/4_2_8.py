# Написать программу, которая просит пользователя ввести ряд положительных чисел. Пользователь
# должен ввести отрицательное число в качестве сигнала конца числового ряда . После того как
# все положительные будут введены , программа должна вывести их сумму.



NUMBERS = int(input('Enter positive number: '))
total = 0

while NUMBERS >= 0 :
    total+=NUMBERS
    NUMBERS = int(input('Enter positive number: '))

print(f'(Sum of entered numbers: ')


