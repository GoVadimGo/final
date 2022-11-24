# Написать цикл , который просит пользователя ввети число. Цикл должен
# должен выполнить 10 итераций и вести учет нарастающего итога введенных чисел.

number = 0

for x in range(10):
    number1 = int(input('Enter number: '))
    number += number1
    print(number)