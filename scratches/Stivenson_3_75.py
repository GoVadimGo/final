# Строка называется палиндромом, если она пишется одинаково в  обоих направлениях. Например, палиндромами в  английском
# языке являются слова «anna», «civic», «level», «hannah». Напишите программу, запрашивающую у пользователя
# строку и при помощи цикла определяющую, является ли она палиндромом.




reverse = ''

message = input('Enter message : ')

for x in message:
    reverse = x + reverse # каждый аргумент приравниваемый x будет добавлятся до reverse .
new = reverse
if new == message:
    print('nice')
else:
    print('nope')
