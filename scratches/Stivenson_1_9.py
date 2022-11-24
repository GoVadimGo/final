# Открыт сберегательный счет в банке под 4 % годовых. Проценты банк расчитывает в конце года и добавляет
# к сумме счета. Написать программу , которая запрашивает пользователя сумму первоначального депозита,
# после чего расчитывает и выводит на экран сумму на счету в конце первого, второго и третьего
# годов. Все суммы должны быть округлены до двух знаков после запятой.

DEPOSIT = int(input('Enter sum of deposit: '))

FIRST_YEAR = (DEPOSIT * 0.04) + DEPOSIT
SECOND_YEAR = (FIRST_YEAR * 0.04) + FIRST_YEAR
THIRD_YEAR = (SECOND_YEAR * 0.04) + SECOND_YEAR
FOURTH_YEAR = (THIRD_YEAR * 0.04) + THIRD_YEAR

print(f'Your savings after First year- {FIRST_YEAR:,.1f}$.\n'
      f'After Second year - {SECOND_YEAR:,.1f}$.\n'
      f'After Third year - {THIRD_YEAR:,.1f}$.\n'
      f'After Fourth year - {FOURTH_YEAR:,.1f}$.')