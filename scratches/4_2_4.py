# Пройденное транспортным средством расстояние можно вычислить следующим образом :
# расстояние = скорость * время
# Например, если поезд движется со скоростью 90 км/час в течение трех часов, то пройденное расстояние
# составит 270 км.
# Написать программу, которая запрашивает у пользователя скорость транспортного
# средства в км/час и количество часов , которое оно двигалось.
# Затем она должна применить цикл для вывода
# расстояния , пройденного транспортным средством для каждого часа этого периода времени.

SPEED = int(input('Enter speed in of the vehicle(km/h) : '))
TIME = int(input('Enter time vehicle spent: '))
DIS = 0
print('Hour\tDistance')
print('--------------')
for x in range(TIME):
    DIS = SPEED * (x+1)
    print(f'{x+1}\t\t{DIS}')
