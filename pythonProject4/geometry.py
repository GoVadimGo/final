# эта программа позволяет выбирать различные геометрические вычисления из меню

# программа geometry импортирует модули circle и rectangle

import circle
import rectangle

# константы для элементов меню

AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

def main():
    # переменная choise управляет циклом и содержит выбор пользователя
    choise = 0
    while choise != QUIT_CHOICE:
        # инструкция show_menu() вызывает функцию show_menu и показывает варианты выбора
        show_menu()
        # получить варианты выбора
        choise = int(input('Выберите вариант : '))
        # выбрать выбранное действие
        if choise == AREA_RECTANGLE_CHOICE:
            radius = float(input('Введите радиус круга : '))
            print(f'Площадь круга {circle.area(radius):.2f} см"2 ')
        elif choise == CIRCUMFERENCE_CHOICE:
            radius = float(input('Введите радиус круга : '))
            print(f'Длина окружности круга {circle.circumference(radius):.2f} см')
        elif choise == AREA_RECTANGLE_CHOICE:
            width = float(input('Введите ширину : '))
            length = float(input('Введите длину : '))
            print(f'Площадь прямоугльника {rectangle.area(length, width):.2f} см"2 ')
        elif choise == PERIMETER_RECTANGLE_CHOICE:
            width = float(input('Введите ширину : '))
            length = float(input('Введите длину : '))
            print(f'Периметр прямоугольника {rectangle.perimetr(width, length):.2f} см')
        else:
            print('Вы ввели неправильный вариант.')


def show_menu():
    print(f'1. Площадь круга \n'
          f'2. Длина окружности круга \n'
          f'3. Площадь прямоугольника \n'
          f'4. Периметр прямоугольника \n'
          f'5. Выход')

main()


