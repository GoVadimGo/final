# Напишите программу, реализующую метод Ньютона для нахождения квад ратного корня числа x, введенного пользователем.
# Алгоритм реализации метода Ньютона следующий:

# Запрашиваем число x у пользователя
# Присваиваем переменной guess значение x / 2
# Пока значение переменной guess не будет обладать должной точностью
# Присваиваем переменной guess результат вычисления среднего между guess и x / guess

# По завершении алгоритма в переменной guess будет находиться определенное приближение вычисления квадратного
# корня из x. Качество аппроксимации при этом будет зависеть только от вашего желания. В нашем случае расхождение
# между значениями guess * guess и  x должно составлять не более 10*–12.

x = int(input('Enter number : '))
guess = x
ep = 0.0000001
found = False

while not found:
    old_guess = guess
    guess = (guess + x/guess) * 0.5
    if abs(guess - old_guess) < ep:
        found = True
        print(guess)