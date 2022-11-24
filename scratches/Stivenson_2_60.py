# day_of_the_week =  (year + floor((year - 1)/4)- floor((year - 1)/100) + floor((year - 1)/400))%7.
# Формула может быть использована для определения дня недели, соответствующего 1 января заданного года.
# В результате мы получим целое число, представляющее день недели от воскресенья (0) до субботы (6).
# Используйте эту формулу для написания программы, запрашивающей
# у пользователя год и выводящей на экран день недели, на который в заданном
# году приходится 1 января. При этом на экран вы должны вывести не числовой эквивалент дня недели,
# а его полное название.
import math
list = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday') # список дней недели
year = int(input('Введите год плз : '))

day_of_the_week =  (year + math.floor((year - 1)/4)- math.floor((year - 1)/100) + math.floor((year - 1)/400))%7
# Формула может быть использована для определения дня недели, соответствующего 1 января заданного года.
# В результате мы получим целое число, представляющее день недели от воскресенья (0) до субботы (6).
print(list[day_of_the_week-1]) # берем из листа агрумент под номером, что получили из формулы , а так как
# в листе счет начинается с нуля ,а из формулы мы получаем минимальную цифру 1 , то минусуем полученное число на 1.