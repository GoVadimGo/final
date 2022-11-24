# Разработайте программу, запрашивающую у пользователя день и месяц –
# сначала месяц в текстовом варианте, затем номер дня. На выходе
# программа должна выдать название сезона, которому принадлежит выбранная дата.

MONTH = input('Enter month : ')
DAY = int(input('Enter day : '))

if MONTH == 'January' or MONTH == 'February':
    print('Winter')
elif MONTH == 'March': # проверяем одно условие
    if DAY > 21:  # затем второе
        print('Spring')
    else:
        print('Winter')
elif MONTH == 'April' or MONTH == 'May':
    print('Spring')
elif MONTH == 'June':
    if DAY > 21:
        print('Summer')
    else:
        print('Spring')
elif MONTH == 'July' or MONTH == 'August':
    print('Summer')
elif MONTH == 'September':
    if DAY > 21:
        print('Autumn')
    else:
        print('Summer')
elif MONTH == 'October' or MONTH == 'November':
    print('Autumn')
elif MONTH == 'December':
    if DAY > 21 :
        print('Winter')
    else:
        print('Autumn')

