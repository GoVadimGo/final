# программа демонстрирует преобразование градусов в радианы

import math

def main():
    DEG = int(input('Enter degrees : '))
    RAD = math.radians(DEG)
    print(f'{DEG} degrees is equal {RAD:.2f} radians. ')
main()