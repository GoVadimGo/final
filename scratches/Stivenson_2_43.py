# Запросите у пользователя  частоту звука. Если введенное значение укладывается
# в диапазон ±1 Гц от значения в  таблице, выведите на экран название
# соответствующей ноты. В  противном случае сообщите пользователю,
# что ноты, соответствующей введенной частоте, не существует. В данном
# упражнении можно ограничиться только нотами, приведенными в таблице.
# Нет необходимости брать в расчет другие октавы.

C = 261.63
D = 293.66
E = 329.63
F = 349.23
G = 392.00
A = 440.00
B = 492.88
LIMIT = 1
GET = float(input('Enter frequency : '))

if GET <= C + LIMIT and GET >= C - LIMIT:
    print('Вы ввели ноту C.')
elif GET <= D + LIMIT and GET >= D - LIMIT:
    print('Вы ввели ноту D')
elif GET <= E + LIMIT and GET >= E - LIMIT:
    print('Вы ввели ноту E ')
elif GET <= F + LIMIT and GET >= F - LIMIT:
    print('Вы ввели ноту F ')
elif GET <= G + LIMIT and GET >= G - LIMIT:
    print('Вы ввели ноту G ')
elif GET <= A + LIMIT and GET >= A - LIMIT:
    print('Вы ввели ноту A ')
elif GET <= B + LIMIT and GET >= B - LIMIT:
    print('Вы ввели ноту B ')
else:
    print('Ты охуел так долго над этим заданием сидеть?!!?!?!?!')


