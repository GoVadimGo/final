# Написать програмный код , который предлагает пользователю ввести число в диапазоне
# от 1 до 100 и проверяет допустимость введенного значения.

numm = int(input('Enter number bigger 1 and smaller 100: '))

while numm < 1 or numm > 100:
    print('Error ,enter again ',end='')
    numm = int(input())