# Написать программу, которая выводит таблицу температур по шкале Цельсия от 0 до 20 и их
# эквиваленты по Фаренгейту. Формула преобразования температуры из шкалы Цельсия
# в шкалу Фаренгейта
# F = (9/5)*C + 32
# Для вывода этой таблицы программа должна применить цикл.

print('Celsius\tFaherheit')
print('------------------')
for c in range (21):
    for y in range(1):
        FAR = (9 / 5) * c + 32
        print(f'{c}\t\t{FAR:.1f}')
