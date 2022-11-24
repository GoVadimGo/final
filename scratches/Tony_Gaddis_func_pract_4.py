# эта программа демонстрирует функцию sqrt

import math

def main():
    num = int(input('Enter number : ')) # получаем от пользователя число и присваиваем его переменной
    result = math.sqrt(num)  # функция принимает аргумент от num , возвращает квадратный корень , который присваивается
    # переменной result
    print(f'Sqrt of {num} is {result}')
main()