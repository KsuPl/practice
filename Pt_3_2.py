c = int(input("Введите число: "))
fib = lambda n, a=0, b=1: [a] + fib(n, b, a + b) if b <= n else [a]
print('Ряд Фибоначчи до числа ', c, ':')
print(*fib(c), sep=', ')
