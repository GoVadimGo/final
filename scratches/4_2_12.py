# В математике запись в форме n! обозначает факториал неотрицптельного целого числа n.
# Факториал n - это произведение всех неотрицательных чисел от 1 до n.
# Например - 7! = 1 * 2 * 3 * 4 * 5 * 6 * 7 = 5040
# Написать программу, которая позволяет пользователю ввести неотрицательное целое число ,
# а затем применяет этот цикл для вычисления факториала этого числа и показывает факториал.



NUM = int(input('Enter number: ')) # Задаем факториал или предел
factorial = 1 # Задаем начальный фокториал
for x in range(1,NUM+1):
        factorial = factorial * x  # Берем начальный факториал и умножаем его с первым значнием в списке
# Потом берем полученное значение и перемножаем его со вторым значением и т.д
print(factorial)