# Написать цикл while , который просит пользователя ввести два числа .
# Числа должны быть сложены , и показана сумму . Цикл должен запрашивать
# у пользователя , желает ли он выполнитьт операцию ещё раз . Если да ,
# то цикл должен повториться ,в противном случае он должен завершиться.

# задать флаг , продолжнающий процесс процесс

DECISION = 'yes'

while DECISION == 'yes':
    first = int(input('Enter first number: '))
    second = int(input('Enter second number: '))
    summ = first + second
    print(f'Sum: {summ}')
    DECISION = input('Do you want to proceed? Type yes if agree: ')
