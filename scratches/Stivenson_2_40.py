# Создайте программу, в которой пользователь будет вводить уровень
# шума в децибелах. Если введенное им значение будет в точности совпадать
# с одним из значений в приведенной таблице, необходимо вывести,
# чему соответствует указанный уровень громкости. Если значение попадет
# между уровнями в таблице, нужно сообщить, между какими именно. Также
# программа должна выдавать корректные сообщения, в случае если введенное
# пользователем значение окажется ниже минимального или больше максимального.
# Отбойный молоток 130 дБ
# Спортбайк 106 дБ
# Будильник 70 дБ
# Тихая комната 40 дБ

HAMMER = 130
MOTOR = 106
ALARM = 70
ROOM = 40

DB = int(input('Enter dB: '))

if DB > HAMMER:
    print('dB too high')
elif DB == HAMMER:
    print('dB in range of Rock-Drill.')
elif DB < HAMMER and DB > MOTOR:
    print('dB in range of Rock-Drill and Sport Bike.')
elif DB == MOTOR:
    print('dB in range of Sport Bike.')
elif DB < MOTOR and DB > ALARM:
    print('dB in range of Sport Bike and Alarm.')
elif DB == ALARM:
    print('dB in range of Alarm.')
elif DB < ALARM and DB > ROOM:
    print('dB in range of Alarm and Quite Room.')
elif DB == ROOM:
    print('dB in range of Quite Room.')
else:
    print('Too quite.')
