def main():
    num1 = int(input('Enter number 1 : ')) # получаем от пользовтеля числа
    num2 = int(input('Enter number 2 : '))
    quant = check(num1,num2) # вызываем функцию check передавая два числа в качестве аргумента , возвращаемое
    # функцией значение присваивается переменной quant
    if quant is None: # инструкция if определяет , равна ли переенная quant значению none
        print('Деление на 0 невозможно.') # если это так , то на экран выводится сообщение
    else: # в противном случае выводится результат деления
        print(f'Число {num1} делить на {num2} равняется {quant}. ')

def check(n1,n2):  
    if n2 == 0:
        status = None
    else:
        status = n1 / n2
        return status

main()