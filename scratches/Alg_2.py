






def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        smallest = arr[i]
        smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arrapop(smallest))
    return newArr

list = [10,2,56,87,123,3,87,33]

print(selectionSort(list))