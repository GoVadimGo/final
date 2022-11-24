# Ваша программа должна запрашивать у пользователя координаты клетки. Используйте условное
# выражение для определения того, с какой клетки – белой или черной – начинается столбец. Затем при помощи обычной
# арифметики необходимо определить цвет конкретной клетки. Например,  если пользователь ввел a1, программа
# должна определить,что клетка с этими координатами черная. Если d5 –белая.

NUM = int(input('Enter number : '))
LETTER = input('Enter letter : ')

numbers = range(1,9)
letters = ['a','b','c','d','e','f','g','h']
if LETTER not in letters:
    print('Letters not in list.')
elif NUM not in numbers:
    print('Numbers not in list.')
else:
    letters_index = letters.index(LETTER)
    numbers_index = numbers.index(NUM)
    if letters_index %2 == numbers_index %2:
        print('Black')
    else:
        print('White')
