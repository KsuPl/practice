a = int(input('Введите число: '))
temp = a
s = ''
arr = []
while temp > 0:
    n = temp % 10
    arr.append(n)
    temp //= 10
arr1 = sorted(arr, reverse=True)
for i in range(len(arr1)):
    s += str(arr1[i])
print(s)
