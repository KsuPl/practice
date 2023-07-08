a = int(input('Введите начальное значение: '))
b = int(input('Введите конечное значение: '))
s = [x**2 for x in [i for i in range(a, b+1)]]
print(s)
