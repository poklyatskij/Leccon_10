"""
a = 8
b = 10
c = 12
d = 18

dividend = ((-3 + a ** 2) * b - 2 ** 3)
divider = (c - 2 * d)
res = dividend / divider

print(res)


minutes = int(input('Введите количество минут: '))
hours = minutes // 60
rest_minutes = minutes % 60

print('Часов:', hours)
print('Осталось минут:', rest_minutes)


n = int(input('Введите номер билета: '))

n1 = n // 100000
n2 = (n % 100000) // 10000
n3 = (n % 100000) // 1000
n4 = (n % 100000) // 100
n5 = (n % 100) // 10
n6 = n % 10

if n1 + n2 + n3 == n4 + n5 + n6:
    print('yes')
else:
    print('no')

"""

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

print(a, b)

a = a + b
b = a - b
a = a - b

print(a, b)


