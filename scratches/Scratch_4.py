
n = int(input('Enter positive number : '))
m = int(input('Enter another positive number: '))

if n < m:
    d = n
else:
    d = m
n = n % d
m = m % d

print(n,m,d)










