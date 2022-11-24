


YEAR = int(input('Enter year : '))

if YEAR %400 ==0:
    flag = True
elif YEAR %100 ==0:
    flag = False
elif YEAR %4 == 4:
    flag = True
else:
    flag = False

if flag:
    print(flag)
else:
    print(flag)