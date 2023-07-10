a = int(input('Введите начало диапазона: '))
b = int(input('Введите конец диапазона: '))
arr = []
for i in range(a, b + 1):
    arr.append(i)
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            arr.remove(i)
            break
print(arr)
