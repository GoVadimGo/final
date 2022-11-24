# Идея шифрования была совершенно тривиальной и заключалась в циклическом сдвиге букв на три позиции. В итоге
# буква A превращалась в D, B – в E, C – в F и т.д. Последние три буквы алфавита переносились на начало. Таким
# образом, буква X становилась A, Y – B, а Z – C. Цифры и другие символы не подвергались шифрованию. Напишите программу,
# реализующую код Цезаря. Позвольте пользователю ввести фразу и количество символов для сдвига, после чег выведите
# результирующее сообщение. Убедитесь в том, что ваша программа шифрует как строчные, так и  прописные буквы. Также
# должна быть возможность указывать отрицательный сдвиг, чтобы можно было использовать вашу программу для расшифровки фраз.


# создать переменную с инструкцией ввода сообщения

message = input('Введите сообщение, которое надо зашифровать : ')

# создать переменную с инструкцией ввода цифры

shift = int(input('Введите цифру для сдвига букв : '))

# создать переменную для накопления зашифрованных букв

new_message = ''

# создать цикл со счетчиком повторений

for ch in message :
    # тело цикла будет переборка каждой буквы сообщения с помощью алгоритма, присвоения ей нового значения и сохранения в новой переменной

    # создаем управляющую структуру , с инструкцией if , условием которой будет находится ли итерируемая буква в области букв алфавита
    # так же условие являются ли буквы большие или маленькие.

    if ch >= 'a' and ch <= 'z':  # если переменная ch получает литерал от a до z

    # алгоритм таков, что берется номер буквы ,от которой отнимается номер буквы "а" или "А". Результат чего присваивается
    # новой переменной.
        pos = ord(ch) - ord('a')

    # далее к частному с остатком на 26(количество букв в ряду) суммы полученной позиции и шага добавляется номер буквы 'a'

        pos = (pos+ shift) % 26 + ord('a')

    # полученную цифру мы конвертируем обратно в букву и скидываем её в список .

        new_cr = chr(pos)

        new_message += new_cr

    # теперь создаем структуру управление, условием которого будут большие буквы алфавита

    elif ch >='A' and ch <= 'Z':

        # такой же алгоритм . Вычитаем цифру буквы от цифры "а" и приравниваем полученны результат переменной.
        pos = ord(ch) - ord('A')
        # к частному с остатком на 26 суммы полученной позиции и сдвигу добавляем "а" цифру.
        pos = (pos + shift)% 26 + ord('A')
        # переделываем цифру на букву и приравниваем результат новой переменной
        new_ch = chr(pos)
        # закидываем букву в накопитель
        new_message += new_ch

    # создаем последнее управление, условием которого будет скидывание всех остальных символов в накопитель.


    else:
        new_message += ch

# показываем результат

print(new_message)
        












