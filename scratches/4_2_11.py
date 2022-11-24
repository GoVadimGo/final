# Если умеренно активный человек будет сокращать свое потребление в калориях на 500 калорий в день,
# то, как правило , он может похудеть примерно на 1.5 кг в месяц. Написать программу , которая позволяет
# пользователю ввести его исходную массу и затем создает и выводит таблицу , показывающую , каким будет
# его ожидаемая масса в конце каждого месяца в течение следующих 6 месяцев , если он продолжит
# придерживаться этой диеты.

months = ['End of Oct' , 'End of Nov', 'End of Dec' ,
          'End of Jan' , 'End of Feb' , 'End of Mar'] # создать список итерируемых месяцев.
MONTHLY = 1.5 # Задать коэфицент похудания.

MASS = int(input('Enter your mass in kg: ')) # Запросить исходную массу.

sport = MASS - MONTHLY # Расчитать массу при учете похудания.
for x in months:
    for y in range(1):
        print(f'{x}\t{sport:.1f}')
        sport-=MONTHLY # Отнять от полученной массы 1.5 кг и обновить переменную
