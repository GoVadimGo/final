# функция area принимает ширину и длину прямоугольника в качестве аргументов и возвращает площадь прямоугольника

import test__main__name__



def area(width,length):
    return width * length

# функция perimeter принимает ширину и длину прямоугольника в качестве аргументов и возвращает его периметр

def perimeter(width,length):
    return 2 * (width + length)

# функция main используется для тестирования другой функции.

def main():
    width = float(input('Enter width : '))
    length = float(input('Enter length : '))
    print(f'Area is {area(width,length):.2f}')
    print(f'Perimeter is {perimeter(width,length):.2f}')
    print(test__main__name__.sqr(length))

# вызываем функцию main только если файл запускается как отдельная программа

if __name__ == '__main__':
    main()