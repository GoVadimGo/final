# Разработайте программу, запрашивающую у пользователя букву латинского алфавита. Если введенная
# буква входит в следующий список (a, e, i, o или u), необходимо вывести сообщение о том, что эта
# буква гласная. Если была введена буква y, программа должна написать, что эта буква может
# быть как гласной, так и согласной. Во всех других случаях должно выводиться
# сообщение о том, что введена согласная буква.

list = ('a','e','i','o','u')

STRING = input('Enter letter : ')

if STRING in list:
    print('You entered vowel')
elif STRING == 'y':
    print('You entered either vowel or consonant')
else:
    print('You entered consonant')
