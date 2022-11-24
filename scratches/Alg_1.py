# binary_search функция берет отсортированный массив и обьект . Если обьект в массиве , функция возвращает позицию этого обьекта.
# отслеживаем , какую часть массива необходимо просмотреть.
import math
def binary_search(list, item):
    low = 0  # это весь массив , начинается с 0 .
    high = len(list)-1 # и заканчивается количеством обьектов в массиве. Тоесть все цифры ,которые мы просматриваем.
    # low high отслеживает какую часть массива мы сканируем.

    while low <= high: # пока мы не сузили поиск поиск до одного обькта.( после low идет сразу high)
        mid =math.floor((low + high) /2)  # каждый раз мы проверяем обьект в середине.
        guess = list[mid] # создаем переменную guess и передаем переменной обьект из массива, который находится в середине.
        if guess == item: # если это и есть то, что мы искали, возвращаем этот обьект.
            return mid
        if guess > item: # если значение переменной больше нашего обьект
            high = mid - 1  # меняем наш верхний лимит поиска ,отбрасывая все обьекты в массиве ,что выше значения mid.
            # и делая mid новым верхним пределом.
        else: # если guess меньше того ,что мы искали, то
            low = mid + 1  # меняем наш нижний лимит поиска, отбрасывая все обьекты в массиве, что ниже значения mid.
            # и делая наш mid новым нижним пределом.
    return None

my_list = [1,3,5,7,9,12]

print(binary_search(my_list, 8))
print(binary_search(my_list, 8))

