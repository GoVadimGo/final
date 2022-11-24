# Разработайте программу, запрашивающую у пользователя день и месяц –
# сначала месяц в текстовом варианте, затем номер дня. На выходе
# программа должна выдать название сезона, которому принадлежит выбранная дата.

from datetime import timedelta , date  # импортируем из модуля datetime классы timedelta и date
YEAR = 2022

list =('January','February','March','April','May','June','July','August','September','October','November','December')
# создаем лист с месяцами
MONTH = input('Enter month : ') # вводим месяц
DAY = int(input('Enter day : ')) # вводим день
if MONTH in list: # находим положение месяца в списке по индексу который будет приравнен к введненному месяцу .
    index = list.index(MONTH)+1

t_x = date(year=YEAR, month= index , day= DAY)  # задаем переменную с датами
t1 = date(year=YEAR, month= 12 , day= 21)  # диапазоны времен года
t2 = date(year=YEAR, month = 9 , day = 21)
t3 = date(year=YEAR, month= 6 , day= 21)
t4 = date(year=YEAR, month= 3 , day= 20)


if t_x>t3 and t_x < t2:   # сравниваем новую переменную с датами
    print('Summer')
elif t_x > t2 and t_x < t1:
    print('Autumn')
elif t_x > t4 and t_x < t3:
    print('Spring')
elif t_x > t1 or t_x < t4:
    print('Winter')
