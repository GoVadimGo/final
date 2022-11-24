# модуль circle содержит функции ,которые принимают аргументы для вычисления площади
# круга или длины окружности

import math

# функция area принимает радиус в качестве аргумента и возвращает площадь круга

def area(radius):
    return math.pi * radius**2

# функция circumference принимает радиус в качестве аргумента и возвращает длину окружности

def circumference(radius):
    return 2 * math.pi * radius