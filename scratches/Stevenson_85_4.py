# Напишите функцию, принимающую на вход длины двух катетов прямоугольного
# треугольника и возвращающую длину гипотенузы, рассчитанную по теореме Пифагора. В главной
# программе должен осуществляться запрос длин сторон у  пользователя, вызов функции и  вывод на экран
# полученного результата.

import math

def main():
    A = float(input('A side : '))
    B = float(input('B side : '))
    print(f'Hypotenuse of triangle is {hypo(A,B):.2f}')

def hypo(A,B):
    return math.hypot(A,B)

main()