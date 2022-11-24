# Напишите программу для расчета индекса массы тела (body mass index –
# BMI) человека. Пользователь должен ввести свой рост и вес, после чего вы
# используете одну из приведенных ниже формул для определения индекса.
# Если пользователь вводит рост в дюймах, а  вес в  фунтах, формула будет
# следующей:  BMI = WEIGHT / (HEIGHT**2)

WEIGHT = int(input('Enter your weight in KG: '))
HEIGHT = float(input('Enter your height in M: '))
BMI = WEIGHT / (HEIGHT**2)
print(f'Your Body Mass Index is {BMI:.1f}.')