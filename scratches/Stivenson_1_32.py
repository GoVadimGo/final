# Разработайте программу, запрашивающую у  пользователя целое четырехзначное
# число и подсчитывающую сумму составляющих его цифр. Например, если пользователь введет число
# 3141, программа должна вывести следующий результат: 3 + 1 + 4 + 1 = 9.

NUM = input('Enter number : ') # We read the input as string and as string is an iterable object we can
# find the each digit by using the position starting from 0 as first position
sum = 0
for i in range(0,len(NUM)):
    sum= sum + int(NUM[i])
print(f'Sum of digits in number : {sum}')

NUM = int(NUM)
sum_1 = 0
while(NUM>0):
    i = NUM%10
    sum_1 +=i
    NUM=NUM//10
print(sum_1)
