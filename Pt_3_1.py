import random
n = int(input('Введите количество чисел: '))
arr = [random.randint(10, 100) for i in range(n)]
print(arr)
a = lambda x: sum(x) / len(x)
print(a(arr))
