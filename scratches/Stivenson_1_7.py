# Написать программу, запрашивающую у пользователя число и подсчитывающую сумму натуральных положительных чисел
# от 1 до введенного пользователем значения. Сумма первых n положительных чисел может быть расчитана по формуле
# sum = ((n)(n+1))/2

num1 = int(input('Enter number: '))

sum = ((num1)*(num1+1))/2

print(sum)