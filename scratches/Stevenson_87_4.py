# Интернет-магазин предоставляет услугу экспресс-доставки для части своих товаров по цене $10,95
# за первый товар в  заказе и  $2,95  – за все последующие. Напишите функцию, принимающую в
# качестве единственного параметра количество товаров в заказе и  возвращающую общую
# сумму доставки. В основной программе должны производиться запрос количест ва позиций в  заказе
# у пользователя и  отображаться на экране сумма доставки.

FIRST = 10.95
RATE = 2.95

def main():
    purch = int(input('Количество покупок : ')) # принимаем от пользователя количество покупок и отправляем
    print(f'Сумма доставки составляет {total(purch):.2f} $') # в функцию , принимаем результат.

def total(purch):
    if purch == 1:
        return FIRST
    elif purch > 1:
        return FIRST + ((purch - 1 ) * RATE)
    else:
        return 0

main()

