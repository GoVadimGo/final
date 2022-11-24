from math import sqrt

first_X = float(input('X: '))
first_Y = float(input('Y: '))

perimetr = 0

counter_X = first_X
counter_Y = first_Y

X = input('Enter X dot (space to quit) : ')
while X != '':
    Y = float(input('Enter Y dot : '))
    X = float(X)
    side = sqrt((X - counter_X) ** 2 + (Y - counter_Y) ** 2)
    counter_X = X
    counter_Y = Y
    perimetr += side
    X = input('Enter X dot (space to quit) : ')
side = sqrt((first_X - counter_X) ** 2 + (first_Y - counter_Y) ** 2)
perimetr += side

print(f'Perimetr : {perimetr:.2f}')
print(f'counter X , counter Y : {counter_X} , {counter_Y}')
