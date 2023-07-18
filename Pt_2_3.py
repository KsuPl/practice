a = int(input('Введите число: '))
sum = 0
temp = a
while temp > 0:
    n = temp % 10
    sum += n ** 3
    temp //= 10
if a == sum:
    print(a, 'является числом Армстронга')
else:
    print(a, 'не является числом Армстронга')
