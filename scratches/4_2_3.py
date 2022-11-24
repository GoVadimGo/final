# Написать программу , которая просит пользователя ввести сумму, выделенную им на один месяц.
# Затем цикл должен предложить пользователю ввести суммы отдельных статей его расходов за
# месяц и подсчитать их нарастающим итогом. По завершению цикла программа должна вывести
# сэкономленную или перерасходованную сумму.

SUMM = int(input('Enter sum of money you get monthly: '))
CHARGES = int(input('Enter number of individual charges this month: '))
SUMM_X = 0.0

if CHARGES > 0:
    for x in range(CHARGES):
        SUMM_Y = int(input(f'Enter sum of your {x+1} individual charge: '))
        SUMM_X+=SUMM_Y
    if SUMM_X > SUMM:
        print(f'You spent over {SUMM_X-SUMM}$ ')
    elif SUMM_X < SUMM:
        print(f'You saved {SUMM-SUMM_X}$')
elif CHARGES == 0:
    print('You saved alot!')

