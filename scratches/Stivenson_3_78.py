# Гипотеза Коллатца .
import math


number = int(input('Enter positive number : '))

while number !=0 and number >0: # внешний цикл для выхода 0 или отрицптельное число
   while number != 1:  # в задании не очень четко обьяснили задачу. Пока последний элемент последовательности...
# смысл гипотезы в том, что путем двух алгоритмов вывести любое положительное число к единицы.
# Мы вводим цифру и начинаем путем цикла while итерировать цифру выполняя один алгоритм либо второй до тех
# пор пока цифра не станет единицей.
# Смысл первого алгоритма заключается в том, что если цифра четная , то делим цифру на 2 ,округляя вниз
       if number % 2 == 0:
           number = math.floor(number / 2 )
# смысл второго алгоритма в том, что если цифра нечетная, то умножаем число на 3 и прибавляем единицу.
       elif number % 2 == 1 :
           number = (number * 3 ) + 1
# конце цикла выводим числа
       print(number)
   number = int(input('Enter positive number: '))