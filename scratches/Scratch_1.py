






list = [9,-2,7,6,5,4,3,2,1]
smallest = list[0]
smallest_index = 0
for i in range(1, len(list)):
    if list[i] < smallest:
        smallest = list[i]
        smallest_index = i
    print(smallest)
