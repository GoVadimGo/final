# Написать цикл, который вычисляет сумму приведенного ниже числового ряда :
# 1/30 + 2/29 + 3/28 + 4/27 ... 30/1

x = 1
y = 30
z = 1 / 30

for a in range (29):
      x+=1   # Задаем новый x
      y-=1   # Задаем новый y
      z1=x/y   # Делаем новую переменную
      z += z1   # Обновляем старый z плюсуя с z1  и т.д
      if x == 30:   # Когда числитель доходит до 30 , даем команду отобразить все сложения
          print(f'{z:.1f}')



