# Напишите программу, которая будет запрашивать у пользователя рейтинг
# сотрудника и выводить соответствующее значение из приведенной таблицы.
# Также необходимо показать сумму прибавки сотрудника. При вводе некорректного
# значения рейтинга программа должна об этом сообщать.

RATING = [0.0,0.4,0.6]
SAL = 2400
SCORE = float(input('Введите свой рейтинг (0.0,0.4,0.6 или выше) : '))
if SCORE in RATING or SCORE > 0.6:
    if SCORE == 0.0:
        print(f'У Вас низкий уровень и у вас нет прибавки. ')
    elif SCORE == 0.4:
        print(f'Удовлетворительный уровень и Ваша прибавка составляет {0.4*SAL:.2f}$.')
    elif SCORE >= 0.6:
        print(f'Высокий уровень и Ваша прибавка составляет {0.6*SAL:.2f}$.')
else:
    print('Неверный рейтинг.')


