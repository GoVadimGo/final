# Количество дней в месяце варьируется от 28 до 31. Очередная ваша программа
# должна запрашивать у пользователя название месяца и отображать
# количество дней в нем. Поскольку годы мы не учитываем, для февраля можно вывести
# сообщение о том, что этот месяц может состоять как из 28, так и из 29 дней,
# чтобы учесть фактор високосного года.

list =('January','February','March','April','May','June','July','August','September','October','November','December')
from datetime import datetime
from calendar import monthrange

current_year = datetime.now().year
month = input('Enter month: ')
if month in list:
# находим индекс элемента в списке. Используем метод index()  Список - list ()
    index = list.index(month)
index+=1
days = monthrange(current_year, index)[1]
print(f'In {month} is {days} days.')




