# Попробуем определить буквенный номинал оценки по его числовому эквиваленту. Убедитесь
# в том, что ваша программа будет обрабатывать числовые значения между
# указанными в таблице. В этом случае оценки должны быть округлены до
# ближайшей буквы. Программа должна выдавать оценку A+, если введенноем пользователем
# значение будет 4,0 и выше.

def closest(NUMBERS,NUM):
    return NUMBERS[min(range(len(NUMBERS)),key = lambda i :abs(NUMBERS[i]-NUM))] # We use min method and apply
# a key that finds the absolute difference of each element with NUMBER list and returns the element
# having minimum difference .
# abs () function is used to return absolute value of a number
# Use key to sort data using lambda function

NUMBERS = [0,1.0,1.3,1.7,2.0,2.3,2.7,3.0,3.3,3.7,4.0,5]
LETTERS = ['F','D','D+','C-','C','C+','B-','B','B+','A-','A','A+']
NUM = float(input('Enter number: '))
NUM_1 = closest(NUMBERS,NUM)
NUM_1 = int(NUM_1)
index = NUMBERS.index(NUM_1)
print(f'Ваша оценка в числовом значении : {LETTERS[index]}.')