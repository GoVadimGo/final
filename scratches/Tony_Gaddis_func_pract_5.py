# эта программа демонстрирует вычисление длинны гипотенузы

import math

def main():
    A = int(input('Enter A side : '))
    B = int(input('Enter B side : '))
    hypo = math.hypot(A,B)
    print(f'Length of hypotenuse is {hypo:.2f}')
main()