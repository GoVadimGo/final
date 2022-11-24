# Запрос у пользователя два целых числа a и b , после чего выводит на экран результаты следующих
# математических операций.
# сумма a и b
# разница между a u b
# произведение a u b
# частное от деления a на b
# остаток от деления a на b
# десятичный логарифм числа на а
# результат возведения числа a в степень b

import math

A = int(input('Enter number a : '))
B = int(input('Enter number b : '))

SUM = A + B
DIFF = A // B
MULTIPLICATION = A * B
DIV = A / B
RESIDUE = A % B
LOG = math.log10(A)
DEGREE = A**B

print(f'{SUM}\n'
      f'{DIFF:.1f}\n'
      f'{MULTIPLICATION}\n'
      f'{DIV:.1f}\n'
      f'{RESIDUE}\n'
      f'{LOG:.1f}\n'
      f'{DEGREE:.1f}')

