# создаем функцию и возвращаем несколько значений

def names():
    first = input('Enter your name : ')
    sec = input('Enter your second name : ')
    return (first,sec)

first_name , second_name = names()

