# Напишите программу для расчета периметра заданного многоугольника.  Начните с запроса у пользователя координат
# x и y первой точки многоугольника. Продолжайте запрашивать координаты следующих точек фигуры, пока пользователь
# не оставит строку ввода координаты по оси x пустой. После ввода каждой пары значений вы должны вычислить длину
# очередной стороны многоугольника и  прибавить полученное значение к будущему ответу. По окончании ввода  необходимо
# вычислить расстояние последней введенной точки до первой, чтобы замкнуть фигуру, и  вывести итоговый результат.

# Расстояние между точками на плоскости можно рассчитать  по теореме Пифагора.
from math import sqrt  # импортируем класс sqrt


perimetr = 0  # создаем накопитель сторон
first_X = float(input('Enter X: '))  # задаем перевую точку Х
first_Y = float(input('Enter Y: ')) # задаем первую точку У
drop_X = first_X # скидываем первую точку Х в новую переменную
drop_Y = first_Y # скидываем первую точку У в новую переменную
# drop_X  после того , как по формуле мы найдем первую сторону ,по формуле пифагора, во втором цикле нам уже не нужна
# первая точка, так как для получения новой стороны мы берем "новую точку" и точку полученную за первую итерацию
# поэтому создаем до цикла создаем "накопитель" "вычитаемой" стороны , тоесть drop_X drop_Y
# после первого использования значения переменной drop_X drop_Y , после формулы пифагора , передаем
# накопителю "вычитаемой" стороны полученные в первой итерации значения . Со второго цикла мы получаем новые точки,
# по формуле пифагора - вычитаем от новых точек накопитель предыдущих и потом обновляем накопитель "старых " точек ,
# что бы потом вычисть новые стороны.
# Когда мы заканчиваем цикл, нам остается соединить самые первые точки с последне введенной точкой , так же по пифагору
# отнимаем от самых первых точек последние точки.



X = input('Enter X: ')  # задаем вторую точку Х
while X != '': # создаем цикл , условием остановки которого будет пробел
        XX = float(X)  # переделываем тип точки на float
        Y = float(input('Enter Y: ')) # задаем вторую точку У
        side = sqrt((XX-drop_X)**2+(Y-drop_Y)**2) # по формуле пифагора находим сторону
        perimetr+=side # скидываем сторону в накопитель
        drop_X = XX # скидываем последне полученную точку в переменную
        drop_Y = Y # скидываем последне полученную точку в переменную
        X = input('Enter X: ') # задаем дальше точки или останавливаемся
side = sqrt((first_X-drop_X)**2+(first_Y-drop_Y)**2) # связываем первые точки с последними
perimetr+=side # скидываем последнюю сторону в накопитель сторон
print(f'{perimetr:.2f}') # показываем периметр








