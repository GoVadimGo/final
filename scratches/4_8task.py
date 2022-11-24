# Написать програмный код , который предлагает пользователю ввести положительное ненулевое число
# и выполняет проверку допустимости входного значения.

numm = int(input('Enter positive number bigger 0 : '))

while numm < 0:
    print('Error,number should be bigger than 0')
    numm = int(input('Enter new number bigger 0: '))
