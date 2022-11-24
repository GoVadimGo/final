def is_inv(mod_num):   # определяем функцию , в качестве аргумента получаем переменную, значение которой присваивается
    # переменной model
    if mod_num != 100 and mod_num != 200 and mod_num != 300:  # проверяем условие
        status = True
    else:
        status = False
    return status  # отправляем результат

model = int(input('Enter available number of model : '))   # получаем аргумент и присваиваем его переменной

while is_inv(model):  # создаем цикл с вызовом функции, передавая ей значение переменной в качестве аргумента и принимая
    # обтрано проверенное условие в качестве true или false .
    print('Available models : 100, 200, 300 ')
    model = int(input('Enter available number of model : ')) # если условие не выполнено, то запрашиваем опять данные
    # и отправляем их в функцию

