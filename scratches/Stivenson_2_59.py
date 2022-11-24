# Разработайте программу, принимающую на вход дату и  выводящую на экран дату, следующую за ней.
# Дату пользователь должен вводить в три этапа: год, месяц и день. Убедитесь, что ваша программа
# корректно обрабатывает високосные годы.

# date2 = date1 + timedelta

from datetime import datetime , timedelta

DAY = int(input('Day '))
MONTH = int(input('Month '))
YEAR = int(input('Year '))

if

if YEAR %400 ==0:
    flag = True
elif YEAR %100 ==0:
    flag = False
elif YEAR %4 == 4:
    flag = True
else:
    flag = False

if flag == False and MONTH == 2 and DAY >28:
    print('Год не високосный и содержит не 29 дней.')
    DAY = int(input('Day '))



date_1= datetime(YEAR,MONTH,DAY) + timedelta(1)
print(datetime.date(date_1))



