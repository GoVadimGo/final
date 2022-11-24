BIT = input('Введите 8 бит , строка для выхода : ')

while BIT != "":
    if BIT.count('1') + BIT.count('0') != 8 or len(BIT) !=8:
        print('Вы ввели неправильный код. Попробуйте заного. ')
    else:
        ones = BIT.count('1')
        if ones % 2 == 0:
            print('Бит четный.')
        else:
            print('Бит нечетный')
    BIT = input('Введите 8 бит , строка для выхода : ')


