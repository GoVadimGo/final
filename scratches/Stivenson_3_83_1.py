# Находим максимумы в случайном ряду чисел из 100 целых чисел и считаем количество обновлений максимального значения

from random import randrange

NUM_ITEMS = 100

# Генерируем и выводим первое число

mx_value = randrange(1, NUM_ITEMS+1)
print(mx_value)

# В этой переменной будем накапливать количество обновлений максимума.

num_updates = 0

# Проходим по числам

for i in range(1 ,NUM_ITEMS):
    # генерируем новое случайное число
    current = randrange(1,NUM_ITEMS+1)
    # если оно превышает текущий максимум
    if current > mx_value:
        mx_value = current
        num_updates += 1
        # отображаем значение с пометкой
        print(current, 'Update')
    else:
        # отображаем значение
        print(current)
# отображаем результаты
print(mx_value, 'Max value')
print(num_updates , 'Number of updates')
