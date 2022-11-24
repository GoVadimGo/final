# Козерог 22 декабря – 19 января                    Рак 21 июня – 22 июля
# Водолей 20 января – 18 февраля                    Лев 23 июля – 22 августа
# Рыбы 19 февраля – 20 марта                        Дева 23 августа – 22 сентября
# Овен 21 марта – 19 апреля                         Весы 23 сентября – 22 октября
# Телец 20 апреля – 20 мая                          Скорпион 23 октября – 21 ноября
# Близнецы 21 мая – 20 июня                         Стрелец 22 ноября – 21 декабря

# Напишите программу, запрашивающую у пользователя дату его рождения
# и выводящую на экран соответствующий знак зодиака.

DAY, MONTH = input('Enter your birthday : ').split()
DAY = int(DAY)
if MONTH == 'December':
    if DAY >= 22 :
        print('CAPRICORN')
    else:
        print('SAGITTARIUS')
elif MONTH == 'January':
    if DAY <= 19:
        print('CAPRICORN')
    else :
        print('AQUARIUS')
elif MONTH == 'February':
    if DAY >= 18 :
        print('AQUARIUS')
    else:
        print('PISCES')
elif MONTH == 'March':
    if DAY >=20:
        print('PISCES')
    else:
        print('ARIES')
elif MONTH == 'April':
    if DAY >= 19:
        print('ARIES')
    else:
        print('TAURUS')

